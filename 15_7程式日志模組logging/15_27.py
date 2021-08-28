"""
15-27.py: list the current level set by level
"""
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s : %(message)s')
logging.debug('logging message, DEBUG')
logging.info("logging message, INNFO")
logging.warning("logging message, WARING")
logging.error('logging message, ERROE')
logging.critical('logging message, CRITICAL')
