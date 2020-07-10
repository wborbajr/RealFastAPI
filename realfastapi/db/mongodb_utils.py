from databases import DatabaseURL
from dynaconf import settings
from loguru import logger
from motor.motor_asyncio import AsyncIOMotorClient

from realfastapi.db.mongodb import db

MONGODB_URL = DatabaseURL(
    f"mongodb://{settings.MONGO_USER}:{settings.MONGO_PASS}@{settings.MONGO_HOST}:{settings.MONGO_PORT}/{settings.MONGO_DB}"
)


async def dbConnect():
    logger.info("Connecting to MongoDB...")
    db.client = AsyncIOMotorClient(
        str(MONGODB_URL),
        maxPoolSize=settings.MAX_CONNECTIONS_COUNT,
        minPoolSize=settings.MIN_CONNECTIONS_COUNT,
    )
    logger.info("Connected！")


async def dbDisconnect():
    logger.info("Disconnecting from MongoDB...")
    db.client.close()
    logger.info("Disconnected！")
