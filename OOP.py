#-*-coding:utf-8-*-
__author__ = 'lulizhou'
# class Person():
#     def __init__(self,name,age,id):
#         self._name=name
#         self._age=age
#         self._id=id
#     def get_name(self):
#         return self._name
#     def get_age(self):
#         return self._age
#     def get_id(self):
#         return self._id
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course

t = Teacher('Alice', 'Female', 'English')
print t.name
print t.course
