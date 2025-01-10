import os
import sys
import logging

logging_str = "[ %(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir,exists=ok)

logging.basicConfig(
    level = logging.INFO,
    format = logging_str,
    
    handlers = [
        logging.Filehandler(log_filepath),
        logging.Streamhandler(sys.stdout)
    ]
)

logger = logging.getlogger("Bone_marrow_survival_prediction")