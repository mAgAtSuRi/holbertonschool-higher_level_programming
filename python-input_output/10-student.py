#!/usr/bin/python3

"""Module to write a student class"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list) and all(isinstance(elem, str) for elem in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
