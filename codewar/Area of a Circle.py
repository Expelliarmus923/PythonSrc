# -*- coding:utf-8 -*-
import math

__author__ = 'lulizhou'

import types,re

def circleArea(r):
    if re.match(r'(^\d+$)|(^\d+.\d+$)', str(r)):
        return round(math.pi*pow(r, 2), 2)
    return False

print(circleArea(43.2673))

def circleArea2(r):
    return round(pi * r ** 2, 2) if type(r) in (int, float) and r > 0 else False

from numbers import Number
def circleArea3(r):
    if isinstance(r, Number):
        if r > 0:
            return round(r**2*math.pi, 2)
        else:
            return False
    else:
        return False
print(circleArea3(43.2))