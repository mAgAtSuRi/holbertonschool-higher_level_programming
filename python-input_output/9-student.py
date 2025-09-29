#!/usr/bin/python3

"""Module to write a student class"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__

students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]

for student in students:
    j_student = student.to_json()
    print(j_student)
    # print(j_student['first_name'])
    # print(type(j_student['first_name']))
    # print(j_student['age'])
    # print(type(j_student['age']))