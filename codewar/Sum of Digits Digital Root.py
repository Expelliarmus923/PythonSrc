# -*- coding:utf-8 -*-
from functools import reduce

__author__ = 'lulizhou'

# digital_root(16)
# => 1 + 6
# => 7
def digital_root(n):
    if n < 10:
        return n
    num = list(map(lambda x: int(x), list(str(n))))
    # m = reduce(lambda x, y: x + y, num)
    m = sum(num)
    return digital_root(m)


def digital_root2(n):
    return n if n < 10 else digital_root(sum(map(int, str(n))))


print(digital_root(13))