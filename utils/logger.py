import logging
import os
from datetime import datetime

# Ensure the logs directory exists
os.makedirs('logs', exist_ok=True)

# Setup logging configuration
logging.basicConfig(
    filename='logs/alerts.log', 
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

def log_intrusion(alert):
    """
    Logs the intrusion details with timestamp.

    Args:
        alert (dict or str): A dictionary containing 'timestamp' and 'summary' keys,
                             or a string describing the intrusion.
    """
    if isinstance(alert, str):
        logging.info(alert)
        print(f"Intrusion detected: {alert}")  # For immediate console feedback
    elif isinstance(alert, dict):
        logging.info(f"{alert['timestamp']} - {alert['summary']}")
        print(f"Intrusion detected: {alert['summary']}")  # For immediate console feedback
