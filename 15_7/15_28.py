"""
15_28.py: track index value change example
"""
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s : %(message)s')
logging.debug("program start")
for i in range(5):
    logging.debug(" now index "+str(i)+" id="+str(id(i)))
logging.debug("program finish")
