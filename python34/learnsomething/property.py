# -*- coding:utf-8 -*-
__author__ = 'lulizhou'


class Student(object):
    def get_score(self):
        print(self._score)

    def set_score(self, score):
        if not isinstance(score, int):
            raise ValueError("必须是整数")
        if score < 0 or score > 100:
            raise ValueError("成绩介于0到100")
        self._score = score


s = Student()
s.set_score(28)
s.get_score()

# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height

screen = Screen()
screen.height = 100
screen.width = 200
print(screen.resolution)