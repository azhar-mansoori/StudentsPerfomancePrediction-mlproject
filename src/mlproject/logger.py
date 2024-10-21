import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"                            #file name 
log_path=os.path.join(os.getcwd(),"logs",LOG_FILE)                                         #file path
os.makedirs(log_path,exist_ok=True)                                                        #creating folder LOGS

LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)                                              #complete log path

logging.basicConfig(                                                                   # format of log
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
