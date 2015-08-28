# -*- coding:utf-8 -*-
__author__ = 'lulizhou'
import asyncio
import  threading

def hello():
    print("Hello asyncio!(%s)" % threading.currentThread())
    r = yield from asyncio.sleep(1)
    print("Hello again(%s)" % threading.currentThread())

loop = asyncio.get_event_loop()
task = [hello(), hello()]
loop.run_until_complete(asyncio.wait(task))
loop.close()