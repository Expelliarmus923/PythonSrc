__author__ = 'lulizhou'
class Fib(object):

    def __init__(self, num):
        a, b, L = 0, 1, []
        for n in range(num):
            L.append(a)
            a, b = b, a + b
        self.numbers = L

    def __str__(self):
        return str(self.numbers)
    __repr__=__str__
    def __len__(self):
        return len(self.numbers)

f = Fib(10)
print f
print len(f)

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score
    @property
    def grade(self):
        if self.score>80:
            return 'A';
        elif self.score>60:
            return 'B';
        else:return 'C'


s = Student('Bob', 59)
print s.grade

s.score = 60
print s.grade

s.score = 99
print s.grade