# -*- coding:utf-8 -*-
from types import MethodType

__author__ = 'lulizhou'


# 给对象动态绑定方法

class Animal(object):
    pass


def run(self, x):
    self.x = x
    print(x + '在跑')


Animal.run = MethodType(run, Animal)
animal = Animal()
animal.run('狗')


# __slots__ 限制实例属性


class Student(object):
    __slots__ = ('name', 'age')


class GraduateStudent(Student):
    __slots__ = ()

s = Student()
s.name = 'mic'
s.age = 28

g = GraduateStudent()
g.score = 25