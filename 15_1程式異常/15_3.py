"""
15_3.py use try-except-else renew design 15_2.py
"""


def division(x, y):
    try:
        ans = x/y
    except ZeroDivisionError:
        print("a divisor cannot be considered zero")
    else:
        return ans  # return the correct execution result


print(division(10, 2))
print(division(5, 0))
print(division(6, 3))
