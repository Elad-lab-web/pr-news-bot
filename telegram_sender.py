import aiohttp
import asyncio
import logging
import os
from datetime import datetime

logger = logging.getLogger(__name__)
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_API = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"

SOURCE_EMOJI = {"ynet": "📰", "ynet_economy": "💼", "walla_news": "📡", "walla_econ": "💹", "mako": "📺", "n12": "📺", "calcalist": "📊", "globes": "💰", "themarker": "📈", "kan": "🎙️", "channel13": "📺", "channel14": "📺"}

def format_digest(client, matches, date):
    if not matches:
        return [f"📋 *סיכום בוקר | {date.strftime('%d.%m.%Y')}*\n\nשלום {client['name']} 👋\n\nלא נמצאו כתבות רלוונטיות היום ✅"]
    direct = [m for m in matches if m.relevance_type == "direct"]
    competitor = [m for m in matches if m.relevance_type == "competitor"]
    industry = [m for m in matches if m.relevance_type == "industry"]
    messages = [f"📋 *סיכום בוקר | {date.strftime('%d.%m.%Y')}*\nלקוח: *{client['name']}*\nסה\"כ: {len(matches)} | 🔴 {len(direct)} | 🟡 {len(competitor)} | 🔵 {len(industry)}\n{'─'*30}"]
    for title, items in [("🔴 *אזכורים ישירים*", direct), ("🟡 *מתחרים*", competitor), ("🔵 *רלוונטי לענף*", industry)]:
        if not items:
            continue
        chunk = f"\n{title}\n"
        for m in items:
            emoji = SOURCE_EMOJI.get(m.article.source, "📰")
            entry = f"\n{emoji} *{m.article.title}*\n_{m.article.source}_ | ציון: {m.score}/10\n💬 {m.reason}\n🔗 [קריאה]({m.article.url})\n"
            if len(chunk) + len(entry) > 3800:
                messages.append(chunk)
                chunk = f"{title} (המשך)\n"
            chunk += entry
        messages.append(chunk)
    return messages

async def send_message(chat_id, text):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(f"{TELEGRAM_API}/sendMessage", json={"chat_id": chat_id, "text": text, "parse_mode": "Markdown", "disable_web_page_preview": False}, timeout=aiohttp.ClientTimeout(total=15)) as resp:
                data = await resp.json()
                return data.get("ok", False)
        except Exception as e:
            logger.error(f"Telegram send failed: {e}")
            return False

async def send_digest(client, matches, date):
    messages = format_digest(client, matches, date)
    chat_id = client["telegram_chat_id"]
    for i, msg in enumerate(messages):
        await send_message(chat_id, msg)
        if i < len(messages) - 1:
            await asyncio.sleep(0.8)
