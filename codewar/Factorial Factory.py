# -*- coding:utf-8 -*-
from functools import reduce

__author__ = 'lulizhou'
# This function should return n!
def factorial(n):
    pass
    if n == 0:
        return 1
    elif n < 0:
        return None
    result = 1

    try:
        for i in range(1, n + 1):
            result *= i
    except:
        return None
    return result


print(factorial(0))


def factorial2(n):
    if n > 0: return reduce(lambda x, y: x * y, range(1, n + 1))
    if n < 0: return None
    return 1