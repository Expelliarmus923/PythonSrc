#-*-coding:utf-8-*-
__author__ = 'lulizhou'
from collections import namedtuple
Point=namedtuple('Point',['x','y'])
p=Point('1','3')
print p.x

from collections import deque
q=deque(['a','b','c'])
q.append('a')
q.appendleft('n')
print q