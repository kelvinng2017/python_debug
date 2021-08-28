"""
15_25.py:list logging export time of every and message
"""
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s : %(message)s')
logging.debug('logging message, DEBUG')
logging.info("logging message, INNFO")
logging.warning("logging message, WARING")
logging.error('logging message, ERROE')
logging.critical('logging message, CRITICAL')
