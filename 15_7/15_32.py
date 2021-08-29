"""
ch15_32.py renew design 15_30.py hide the debug level logging in your program
"""
import logging
logging.basicConfig(level=logging.CRITICAL,
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
