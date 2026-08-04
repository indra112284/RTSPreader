# ==========================================================
# Logger Configuration
# ==========================================================

import logging
import os

from config import LOG_FILE

# Create logs folder if it doesn't exist
os.makedirs("logs", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# Create logger object
logger = logging.getLogger(__name__)