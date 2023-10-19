# logger.py


"""
  This package loggs errors fed into it into the setup file
"""

import logging

def setup_logging(log_file):
    logging.basicConfig(filename=log_file, level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.ERROR)
    logging.getLogger().addHandler(console_handler)

def log_error(error_message):
    logging.error(error_message)
    print("[-] "+ str(error_message))
