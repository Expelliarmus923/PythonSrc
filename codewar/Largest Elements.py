# -*- coding:utf-8 -*-
__author__ = 'lulizhou'


def largest(n, xs):
    """Find the n highest elements in a list"""
    xs.sort()
    # return xs[len(xs)-n: len(xs)]
    return xs[-n:]


print(largest(2, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
