#-*-coding:utf-8-*-
__author__ = 'lulizhou'
import time
def performance(f):
    def fn(*args,**kw):
        t1=time.time()
        r=f(*args,**kw)
        t2=time.time()
        print 'call %s() in %fs' %(f.__name__,(t2-t1))
        return r
    return fn

@performance
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial(10)

#decorator
def decorator(F):
    def new_F(a,b):
        print("input",a,b)
        return F(a,b)
    return new_F
@decorator
def square_sum(a, b):
    return a**2 + b**2
print square_sum(3,4)
import  functools
def log(f):
    @functools.wraps(f)
    def wrapper(*args,**kw):
        print 'call...'
        return f(*args,**kw)
    return  wrapper
@log
def f2(x):
    pass
print f2.__name__