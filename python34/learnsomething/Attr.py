__author__ = 'lulizhou'


class MyObject(object):
    def __init__(self, x):
        self.x = x

    def power(self):
        return self.x * self.x


obj = MyObject(2)
print(hasattr(obj, 'x'))
print(getattr(obj, 'x'))