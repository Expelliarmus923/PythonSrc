# -*- coding:utf-8 -*-
__author__ = 'lulizhou'
# remove vowels
# ('a','e','i','o','u')

def disemvowel(string):
    import re
    my = re.compile(r'([aeiou]+)', re.I)
    string = re.sub(my, '', string)
    return string

# "N ffns bt,\nr wrtng s mng th wrst 'v vr rd" should equal "N ffns bt,\nYr wrtng s mng th wrst 'v vr rd"
print(disemvowel("N ffns bt,\nr wrtng s mng th wrst 'v vr rd"))
print(b'who are you'.translate(None, b'aeiouAEIOU'))

def disemvowel2(string):
    string.maketrans(0, 2)
    return string.translate('aeiouAEIOU')
print(disemvowel2('who are you'))
