# -*- coding:utf-8 -*-
__author__ = 'lulizhou'


def shorter_reverse_longer(a, b):
    if len(a) >= len(b):
        m = a
        a = b
    else:
        m = b
    n = []
    for i in m:
        n.append(i)
    n.reverse()

    return a + ''.join(n) + a


def shorter_reverse_longer2(a, b):
    if len(a) < len(b): a, b = b, a
    return b + a[::-1] + b


print(shorter_reverse_longer("asfsaf", "short"))
