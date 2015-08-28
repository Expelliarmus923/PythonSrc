# -*- coding:utf-8 -*-
__author__ = 'lulizhou'


def tickets(people):
    sum = 0
    for i in range(len(people)):
        if people[i] - 25 <= sum:
            sum += 25
        elif people[i] - 25 > sum:
            return "NO"
    if sum != 25*len(people):
        return "NO"
    return "YES"

print(tickets([25, 25, 50]))