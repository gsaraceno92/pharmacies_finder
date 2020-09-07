import os
import logging
from logging.handlers import RotatingFileHandler
from environs import Env


env = Env()
# Read .env into os.environ
env.read_env()
logging.basicConfig(filename=env.str('LOG_FILE'), level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

handler = RotatingFileHandler(
    os.getenv('LOG_FILE'), maxBytes=env.int('MAX_BYTES_LOG'), backupCount=env.int('BACKUP_FILE_COUNT'))
logger.addHandler(handler)
