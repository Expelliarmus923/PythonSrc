# -*- coding:utf-8 -*-
import re

__author__ = 'lulizhou'

import string

def is_pangram(s):
    s = s.lower()
    total = set()
    for i in range(len(s)):
        if re.match(r'[a-z]+', s[i]):
            total.add(s[i])
    return True if len(total) == 26 else False

def is_pangram2(s):
    print(set(s.lower()))
    print(set(string.ascii_lowercase))
    return set(string.ascii_lowercase) <= set(s.lower())

print(is_pangram("The quick, brown fox jumps over the lazy dog!"))