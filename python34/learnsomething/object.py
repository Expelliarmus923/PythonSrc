import types

__author__ = 'lulizhou'


class Student(object):
    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_score(self):
        return self._score

    def set_score(self, score):
        self._name = score

    def print_score(self):
        print("%s, %s" % (self._name, self._score))

    def get_grade(self):
        if self._score >= 90:
            return 'A'
        elif self._score >= 80:
            return 'B'
        else:
            return 'C'


bart = Student('Bart Simpson', 90)
bart.print_score()
print(bart.get_grade())


class Animal(object):
    def run(self):
        print('Animal is running')


class Dog(Animal):
    def run(self):
        print('Dog is running')


class Cat(Animal):
    def run(self):
        print('Cat is running')


dog = Dog()
dog.run()

cat = Cat()
cat.run()
print(dir(Animal))

print(isinstance(dog, Animal))


def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Dog())
run_twice(Cat())
print(types.FunctionType == type(dog))


def fn():
    pass

print(types.FunctionType == type(fn))