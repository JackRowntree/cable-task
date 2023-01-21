from datetime import datetime, timezone
from functools import wraps
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler("debug.log"), logging.StreamHandler()],
)
logger = logging.getLogger("My Logger")


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        called_at = datetime.now(timezone.utc)
        logger.info(f">>> Running {func.__name__!r} function. Logged at {called_at}")
        to_execute = func(*args, **kwargs)
        logger.info(f">>> Function: {func.__name__!r} executed. Logged at {called_at}")
        return to_execute

    return wrapper
