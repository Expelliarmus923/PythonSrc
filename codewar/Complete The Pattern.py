# -*- coding:utf-8 -*-
__author__ = 'lulizhou'


def pattern(n):
    # Happy Coding ^_^
    all = [x for x in range(1, n + 1)]
    result = ""
    for i in range(0, n + 1):
        if i == 0:
            result += ''.join(str(i) for i in all)
        else:
            telp = all[i:n]
            result += ''.join(str(i) for i in telp)
        result += "\n"

    return result[0:-2]


print(pattern(9))