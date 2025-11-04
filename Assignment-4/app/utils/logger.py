import logging
from logging.handlers import RotatingFileHandler
import os

# Log file directory
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "app.log")

# Basic logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        RotatingFileHandler(log_file, maxBytes=2_000_000, backupCount=5),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("FastAPI-Logger")
logger.info("Logger initialized successfully.")
