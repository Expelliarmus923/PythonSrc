__author__ = 'lulizhou'
#-*-coding:utf-8-*-
import math
def move(x,y,step,angle):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny
x,y = move(100,100,60,math.pi/6)
print x,y
def face(n):
    if n==1:
        return 1
    return n * face(n-1)
print face(10)
def greet(name="World"):
    print "Hello "+name+"!"
greet()
greet("lulizhou")
def average(*args):
    sum=0.0
    if len(args)==0:
        return sum
    for x in args:
        sum+=x
    return sum/len(args)
print average(1,2,3,10)
L = range(1,101)
print L[:10]
print L[2::3]
print L[4:50:5]
print L[:-10]
print L[4::5][-10:]

def firstCharUpper(s):
    return s[0].upper()+s[1:]
print firstCharUpper('hello')