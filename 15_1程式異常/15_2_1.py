"""
15_2_1.py renew desiogn 15_2.py but 
"""


def division(x, y):
    try:  # try -except instruction
        return x/y
    except ZeroDivisionError:  # 除數為0時執行
        print("a divisor cannot be considered zero")


print(division(10, 2))
print(division(5, 0))
print(division(6, 3))
