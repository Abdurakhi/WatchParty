from contextlib import asynccontextmanager

from app.core.logging import get_logger
from app.db.session import engine
from fastapi import FastAPI
from sqlalchemy import text

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("======================================")
    logger.info("Starting WatchParty backend...")
    logger.info("======================================")

    try:
        async with engine.begin() as connection:
            await connection.execute(text("SELECT 1"))

        logger.info("PostgreSQL connected successfully.")

    except Exception:
        logger.exception("PostgreSQL connection failed.")
        raise

    logger.info("Startup completed.")

    yield

    logger.info("======================================")
    logger.info("Stopping WatchParty backend...")
    logger.info("======================================")

    await engine.dispose()

    logger.info("Database engine closed.")

    logger.info("Shutdown completed.")
