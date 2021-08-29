"""
15_24.py renew dessign 15_22.py, cancle show logging export message
"""
import logging
logging.basicConfig(level=logging.DEBUG, format='')
logging.debug('logging message, DEBUG')
logging.info("logging message, INNFO")
logging.warning("logging message, WARING")
logging.error('logging message, ERROE')
logging.critical('logging message, CRITICAL')
