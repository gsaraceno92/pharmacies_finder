import os
import logging
from logging.handlers import RotatingFileHandler
from environs import Env


env = Env()
# Read .env into os.environ
env.read_env()
log_level = logging.DEBUG if env.bool("DEBUG") else logging.INFO
logging.basicConfig(filename=env.str('LOG_FILE'), level=log_level,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

handler = RotatingFileHandler(
    os.getenv('LOG_FILE'), maxBytes=env.int('MAX_BYTES_LOG'), backupCount=env.int('BACKUP_FILE_COUNT'))
logger.addHandler(handler)
