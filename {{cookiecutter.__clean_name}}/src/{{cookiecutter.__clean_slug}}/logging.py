"""Application logging helpers built on Loguru."""

from __future__ import annotations

import os
import sys
from loguru import logger

DEFAULT_LEVEL = "INFO"


def configure_logging(level: str | None = None) -> None:
    """Configure the shared Loguru logger.

    Logging level falls back to the LOG_LEVEL environment variable or INFO.
    """
    log_level = level or os.getenv("LOG_LEVEL", DEFAULT_LEVEL)
    logger.remove()
    logger.add(sys.stdout, level=log_level, colorize=True, enqueue=True)


__all__ = ["logger", "configure_logging"]
