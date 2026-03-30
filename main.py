import asyncio
import logging
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from bot import run_daily_digest

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

async def main():
    scheduler = AsyncIOScheduler(timezone="Asia/Jerusalem")
    scheduler.add_job(run_daily_digest, trigger="cron", hour=7, minute=0, id="daily_digest")
    scheduler.start()
    logger.info("PR News Bot started. Daily digest scheduled for 07:00 IL time.")
    try:
        while True:
            await asyncio.sleep(3600)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()

if __name__ == "__main__":
    asyncio.run(main())
