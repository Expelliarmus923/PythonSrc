# -*- coding:utf-8 -*-
__author__ = 'lulizhou'


def group_check(s):
    right = {'}': 0, ']': 1, ')': 2}
    left = ['{', '[', '(']
    stack = []
    for i in range(len(s)):
        if s[i] in left:
            stack.append(s[i])
        elif len(stack) != 0:
            if left[right[s[i]]] != stack.pop():
                return False
        else:
            return False
    return True if len(stack) == 0 else False


BRACES = {'(': ')', '[': ']', '{': '}'}


def group_check2(s):
    stack = []
    for b in s:
        c = BRACES.get(b)
        if c:
            stack.append(c)
        elif not stack or stack.pop() != b:
            return False
    return not stack


print(group_check("()"))