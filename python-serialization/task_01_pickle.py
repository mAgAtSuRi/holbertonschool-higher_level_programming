#!/usr/bin/python3
import pickle

"""Module Pickling Custom Classes"""


class CustomObject:
    """Class to serialize and deserialize using pickle"""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def serialize(self, filename):
        with open(filename, "w") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        with open(filename) as f:
            return pickle.load(f)
