"""
15_29.py: logging is used to trace the calulation of factorial levels
"""
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s : %(message)s')
logging.debug("program start")


def factorial(n):
    logging.debug("factorial "+str(n)+" 計算開始")
    ans = 1
    for i in range(n + 1):
        ans *= i
        logging.debug('i = '+str(i)+', ans = '+str(ans))
    logging.debug("factorial "+str(n)+" 計算結束")
    return ans


num = 5
logging.debug("factorial("+str(num)+") = "+str(factorial(num)))


logging.debug("program finish")
