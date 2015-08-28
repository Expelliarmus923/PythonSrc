__author__ = 'lulizhou'
def toUppers(L):
    return [x.upper() for x in L if isinstance(x,str)]
print toUppers(['Hello','world','132'])
print [m+n for m in 'ABC' for n in '123']
print [100*n1+10*n2+n3 for n1 in range(1,10) for n2 in range(10) for n3 in range(10) if n1==n3]
def format_name(s):
   return s[0].upper()+s[1:].lower()
print map(format_name,['adam','LISA','barT'])
def prod(x, y):
    return x*y
print reduce(prod, [2, 4, 5, 7, 12])
def is_odd(x):
    return x%2==1
print filter(is_odd,[1,4,6,7,9,12,17])
import math
def is_sqr(x):
    r=int(math.sqrt(x))
    return r*r==x
print filter(is_sqr,range(1,101))
def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0
print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)
name=raw_input()
print 'Hello '+name