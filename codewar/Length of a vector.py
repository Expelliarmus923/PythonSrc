# -*- coding:utf-8 -*-
import math

__author__ = 'lulizhou'

# Test.assert_equals(vector_length([[0, 1],[0, 0]]), 1)
# Test.assert_equals(vector_length([[0, 3],[4, 0]]), 5)
# Test.assert_equals(vector_length([[1, -1],[1, -1]]), 0)
def vector_length(vector):
    return math.sqrt((vector[0][0]-vector[1][0])**2+(vector[0][1]-vector[1][1])**2)
def vector_length2(vector):
    (x1,y1),(x2,y2) = vector
    return ((x1-x2)**2 + (y1-y2)**2) ** .5

print(vector_length([[0, 1], [0, 0]]))