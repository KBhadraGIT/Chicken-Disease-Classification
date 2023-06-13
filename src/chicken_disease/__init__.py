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

logger = logging.getLogger("chickenDisease_Logger")
#================================================================

###Exception handling for the project
import sys,os
def error_message_detail(error, error_detail: sys):
    
    _, _, exc_tb = error_detail.exc_info()
    
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    error_message = f"Error occurred python script name [{file_name}] line number [{exc_tb.tb_lineno}] error message [{str(error)}]"
    
    return error_message

class CDCException(Exception):

    def __init__(self,error_message, error_detail:sys):
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
