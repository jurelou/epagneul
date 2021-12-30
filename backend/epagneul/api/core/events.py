from typing import Callable
import os
from epagneul.common import settings
from loguru import logger
from fastapi import FastAPI

from epagneul.api.core.neo4j import db

def start_app_handler(app: FastAPI) -> Callable:
    """Fastapi start handler."""

    async def start_app() -> None:
        if not os.path.exists(settings.evidences_folder):
            try:
                os.makedirs(settings.evidences_folder)
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        db.bootstrap()


    return start_app


def stop_app_handler(app: FastAPI) -> Callable:
    """Fastapi stop handler."""

    @logger.catch
    async def stop_app() -> None:
        db.close()

    return stop_app
