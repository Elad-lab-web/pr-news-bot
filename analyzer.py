import asyncio
import json
import logging
import os
import re
import aiohttp
from dataclasses import dataclass
from scrapers.rss import Article

logger = logging.getLogger(__name__)

ANTHROPIC_API_URL = "https://api.anthropic.com/v1/messages"
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
BATCH_SIZE = 15

@dataclass
class MatchedArticle:
    article: Article
    relevance_type: str
    score: int
    reason: str

async def analyze_batch(session, articles, client):
    articles_text = "\n\n".join([
        f"[{i+1}] מקור: {a.source}\nכותרת: {a.title}\nתקציר: {a.summary}"
        for i, a in enumerate(articles)
    ])
    prompt = f"""אתה עוזר של משרד יחסי ציבור. עליך לזהות כתבות רלוונטיות ללקוח הבא:

שם הלקוח: {client['name']}
שמות החברה לחיפוש ישיר: {', '.join(client['company_names'])}
מילות מפתח לתחום: {', '.join(client['keywords'])}
מתחרים: {', '.join(client.get('competitors', []))}

להלן {len(articles)} כתבות שנאספו מאתרי תקשורת ישראלים היום:

{articles_text}

עבור כל כתבה, החלט אם היא רלוונטית ללקוח.
סוגי רלוונטיות: direct, competitor, industry
ציון 1-10. כלול רק ציון 5 ומעלה.

החזר JSON בלבד:
{{"results": [{{"index": 1, "relevant": true, "type": "direct", "score": 9, "reason": "הסבר קצר"}}, {{"index": 2, "relevant": false}}]}}"""

    try:
        async with session.post(
            ANTHROPIC_API_URL,
            headers={"x-api-key": ANTHROPIC_API_KEY, "anthropic-version": "2023-06-01", "content-type": "application/json"},
            json={"model": "claude-sonnet-4-20250514", "max_tokens": 1000, "messages": [{"role": "user", "content": prompt}]},
            timeout=aiohttp.ClientTimeout(total=60),
        ) as resp:
            data = await resp.json()
        raw = data["content"][0]["text"].strip()
        raw = re.sub(r"^```json\s*|^```\s*|\s*```$", "", raw, flags=re.MULTILINE).strip()
        parsed = json.loads(raw)
        matched = []
        for r in parsed.get("results", []):
            if not r.get("relevant"):
                continue
            idx = r["index"] - 1
            if 0 <= idx < len(articles):
                matched.append(MatchedArticle(article=articles[idx], relevance_type=r.get("type", "industry"), score=r.get("score", 5), reason=r.get("reason", "")))
        return matched
    except Exception as e:
        logger.error(f"Claude analysis error for {client['name']}: {e}")
        return []

async def find_relevant_articles(all_articles, client):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(0, len(all_articles), BATCH_SIZE):
            batch = all_articles[i:i + BATCH_SIZE]
            tasks.append(analyze_batch(session, batch, client))
            await asyncio.sleep(0.5)
        results = await asyncio.gather(*tasks)
    all_matches = [m for batch in results for m in batch]
    all_matches.sort(key=lambda x: x.score, reverse=True)
    seen = set()
    unique = []
    for m in all_matches:
        if m.article.url not in seen:
            seen.add(m.article.url)
            unique.append(m)
    return unique
