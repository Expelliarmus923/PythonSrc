#-*-coding:utf-8-*-
__author__ = 'lulizhou'
import re
with open('read.txt','r') as f:
    print len(re.split(r'[\s\,\.\:]+',f.read()))