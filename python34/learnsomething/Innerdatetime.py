# -*- coding:utf-8 -*-
__author__ = 'lulizhou'
from datetime import datetime

now = datetime.now()

print(now)
print(now.timestamp())

t = 123124.1

print(datetime.fromtimestamp(t))