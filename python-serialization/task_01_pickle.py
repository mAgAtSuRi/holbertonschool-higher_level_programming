#!/usr/bin/python3
import pickle

"""Module Pickling Custom Classes"""


class CustomObject:
    """Class to serialize and deserialize using pickle"""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        dic = {"Name:": self.name, "Age:": self.age, "Is Student:": self.is_student}
        for k, v in dic.items():
            print(f"{k} {v}")

    def serialize(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        with open(filename, "rb") as f:
            return pickle.load(f)
