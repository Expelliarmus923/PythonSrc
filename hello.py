#!/usr/bin/env python
# -*- coding: utf-8 -*-
'a test module'
__author__ = 'lulizhou'
import sys
def test():
    args=sys.argv
    if len(args)==1:
        print 'HelloWorld!'
    elif len(args)==2:
        print 'Hello,%s!' %args[1]
    else:
        print 'too many argsment!'
if __name__=='__main__':
    test()




