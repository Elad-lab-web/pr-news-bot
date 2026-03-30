import asyncio
import logging
from datetime import datetime, timezone
from scrapers.rss import fetch_all_articles
from analyzer import find_relevant_articles
from telegram_sender import send_digest
from clients.config import get_active_clients, get_all_industries

logger = logging.getLogger(__name__)

async def run_daily_digest():
    now = datetime.now(timezone.utc)
    logger.info(f"=== Starting daily digest: {now.strftime('%Y-%m-%d %H:%M UTC')} ===")
    all_industries = get_all_industries()
    articles = await fetch_all_articles(extra_industries=all_industries)
    if not articles:
        logger.warning("No articles fetched — aborting digest")
        return
    clients = get_active_clients()
    logger.info(f"Processing {len(clients)} active clients")
    for client in clients:
        logger.info(f"Analyzing for client: {client['name']}")
        try:
            matches = await find_relevant_articles(articles, client)
            logger.info(f"Found {len(matches)} relevant articles for {client['name']}")
            await send_digest(client, matches, now)
        except Exception as e:
            logger.error(f"Error processing client {client['name']}: {e}")
        await asyncio.sleep(2)
    logger.info("=== Daily digest complete ===")

if __name__ == "__main__":
    asyncio.run(run_daily_digest())
