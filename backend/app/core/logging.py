import logging
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path

import colorlog
from app.core.config import settings

LOG_DIRECTORY = Path("logs")

LOG_DIRECTORY.mkdir(parents=True, exist_ok=True)


LOG_FORMAT = (
    "%(asctime)s | "
    "%(levelname)-8s | "
    "%(name)s | "
    "%(message)s"
)

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


COLOR_FORMAT = (
    "%(log_color)s"
    "%(asctime)s | "
    "%(levelname)-8s | "
    "%(name)s | "
    "%(message)s"
)


console_formatter = colorlog.ColoredFormatter(
    COLOR_FORMAT,
    datefmt=DATE_FORMAT,
    log_colors={
        "DEBUG": "cyan",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "bold_red",
    },
)


file_formatter = logging.Formatter(
    LOG_FORMAT,
    datefmt=DATE_FORMAT,
)


console_handler = logging.StreamHandler()

console_handler.setFormatter(console_formatter)


application_file_handler = TimedRotatingFileHandler(
    LOG_DIRECTORY / "application.log",
    when="midnight",
    interval=1,
    backupCount=30,
    encoding="utf-8",
)

application_file_handler.setFormatter(file_formatter)


error_file_handler = TimedRotatingFileHandler(
    LOG_DIRECTORY / "errors.log",
    when="midnight",
    interval=1,
    backupCount=30,
    encoding="utf-8",
)

error_file_handler.setLevel(logging.ERROR)

error_file_handler.setFormatter(file_formatter)


logging.basicConfig(
    level=logging.DEBUG if settings.DEBUG else logging.INFO,
    handlers=[
        console_handler,
        application_file_handler,
        error_file_handler,
    ],
)


def get_logger(name: str) -> logging.Logger:
    """
    Returns configured logger.
    """

    logger = logging.getLogger(name)

    logger.propagate = True

    return logger
