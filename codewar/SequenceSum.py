# -*- coding:utf-8 -*-
from functools import reduce

__author__ = 'lulizhou'


def sum_of_n(n):
    sum = 0
    reslut = []
    dir = 1
    m = abs(n)
    if n < 0:
        dir = -1
    for i in range(m+1):
        sum += i
        reslut.append(dir*sum)

    return reslut


def sum_of_n2(n):
    return [(-1 if n < 0 else 1) * sum(xrange(i+1)) for i in xrange(abs(n)+1)]


print(sum_of_n(3))
