"""
ch15_33.py 
"""
import sys  
reload(sys)
sys.setdefaultencoding('utf-8')
import logging
logging.disable(level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s : %(message)s')
logging.debug("program start")


def factorial(n):
    logging.debug("factorial "+str(n)+" calculate start")
    ans = 1
    for i in range(1, n + 1):
        ans *= i
        logging.debug('i = '+str(i)+', ans = '+str(ans))
    logging.debug("factorial "+str(n)+" calculate finish")
    return ans


num = 5
logging.debug("factorial("+str(num)+") = "+str(factorial(num)))
print("factorial("+str(num)+") = "+str(factorial(num)))

logging.debug("program finish")
