# -*- coding: utf-8 -*-
import sys

from loguru import logger

from epagneul.common import settings

log_format = (
    "<level>{level: <6}</level> | <cyan>{name}:{line}</cyan> - <level>{message}</level>"
)
logger.remove()
logger.add(
    sys.stdout,
    level=settings.log.level,
    format=log_format,
)
logger.add(settings.log.file, level=settings.log.level, format=log_format)
