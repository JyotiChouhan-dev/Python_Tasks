from prisma import Prisma
from dotenv import load_dotenv
import os
import logging

# load .env (ensure .env is at project root)
load_dotenv()

# Optional: basic logging setup for this module
logger = logging.getLogger("app.core.config")
if not logger.handlers:
    logging.basicConfig(level=logging.INFO)

# Optional check (won't stop execution, but warns)
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    logger.warning("DATABASE_URL not found in .env — Prisma may fail to connect.")

# Initialize Prisma client here (only once)
prisma = Prisma()  # async client as per schema generator interface = "asyncio"

# Provide small helpers for startup/shutdown to import in main.py
async def connect_db():
    """
    Call this on app startup: await connect_db()
    """
    try:
        logger.info("Connecting to database (Prisma)...")
        await prisma.connect()
        logger.info("Prisma connected.")
    except Exception as e:
        logger.exception("Error connecting Prisma: %s", e)
        raise

async def disconnect_db():
    """
    Call this on app shutdown: await disconnect_db()
    """
    try:
        logger.info("Disconnecting Prisma...")
        await prisma.disconnect()
        logger.info("Prisma disconnected.")
    except Exception as e:
        logger.exception("Error disconnecting Prisma: %s", e)
        # don't re-raise on shutdown
