"15_2.py logging message show warning"
import logging

logging.basicConfig(level=logging.WARNING)  # level is debug
logging.debug('logging message, DEBUG')
logging.info("logging message, INNFO")
logging.warning("logging message, WARING")
logging.error('logging message, ERROE')
logging.critical('logging message, CRITICAL')
