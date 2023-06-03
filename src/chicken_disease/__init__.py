###Logger for the project

import os, sys, logging
from datetime import datetime

#Log file name
LOG_FILE_NAME = f"{datetime.now().strftime('%Y-%m-%d__%H-%M-%S')}"
#Log file directory
LOG_FILE_DIR = os.path.join(os.getcwd(), "logs") 
#Log folder if not created yet
os.makedirs(LOG_FILE_DIR, exist_ok=True)
#Log file path
LOG_FILE_PATH = os.path.join(LOG_FILE_DIR,LOG_FILE_NAME)
#Logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)