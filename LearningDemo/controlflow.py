# -*- coding:utf-8 -*-
__author__ = 'lulizhou'

def fib(n):

    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a+b
fib(2000)