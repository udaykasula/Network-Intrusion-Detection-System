import logging
from datetime import datetime

# Setup logging configuration
logging.basicConfig(filename='intrusion_logs.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')

def log_intrusion(intrusion_details):
    """
    Logs the intrusion details with timestamp.
    
    Args:
        intrusion_details (str): Description or details about the intrusion.
    """
    logging.info(f"Intrusion detected: {intrusion_details}")
    print(f"Intrusion detected: {intrusion_details}")  # For immediate console feedback
