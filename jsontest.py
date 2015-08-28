# -*-coding:utf-8-*-
__author__ = 'lulizhou'
import json

d = dict(name="bob", age=15, score=88)
j = json.dumps(d)
print(j)
print(json.loads(j))


class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Bob', 14, 50)
print(json.dumps(s, default=lambda obj: obj.__dict__))