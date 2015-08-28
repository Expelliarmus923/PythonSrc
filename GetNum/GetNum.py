__author__ = 'lulizhou'
import urllib2
from threading import Timer
import time
def getnum():
    request=urllib2.Request("http://lednit208.aliapp.com/GetNumServlet")
    response=urllib2.urlopen(request)
    d=response.read()
    print d
    with open('data.txt', 'w') as f:
        f.write(d)
timer_interval=1
t=Timer(timer_interval,getnum)
t.start()
while True:
    time.sleep(1)
    getnum()