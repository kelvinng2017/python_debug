"15_22.py logging message show all level"
import logging

logging.basicConfig(level=logging.DEBUG)  # level is debug
logging.debug('logging message, DEBUG')
logging.info("logging message, INNFO")
logging.warning("logging message, WARING")
logging.error('logging message, ERROE')
logging.critical('logging message, CRITICAL')
