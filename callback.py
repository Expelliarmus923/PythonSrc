__author__ = 'lulizhou'
#-*-coding:utf-8-*-
def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1,f2,f3=count()
print f1()
print map(lambda x:x*x,range(1,10))

def log(func):
    def wrapper(*args,**kw):
        print "call %s()" % func.__name__
        return  func(*args,**kw)
    return wrapper
@log
def now():
    print "2015-5-22"

def f():
    print 'call f()....'
    def g():
        print 'call g()...'
    return g
x=f()
x()
def calc_prod(lst):
    def lazy_prod():
        return reduce(lambda x,y :x*y,lst,1)
    return lazy_prod

f = calc_prod([1, 2, 3, 4])
print f()
def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1,f2,f3=count()
print f1()
print f2()
print f3()



