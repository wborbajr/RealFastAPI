from fastapi import FastAPI
from loguru import logger

from realfastapi.db.events import close_db_connection, connect_to_db


def start_app_handler(app: FastAPI) -> Callable:
    """Fastapi start handler."""

    async def start_app() -> None:
        await connect_to_db(app)

    return start_app


def stop_app_handler(app: FastAPI) -> Callable:
    """Fastapi stop handler."""

    @logger.catch
    async def stop_app() -> None:
        await close_db_connection(app)

    return stop_app  # type: ignore
