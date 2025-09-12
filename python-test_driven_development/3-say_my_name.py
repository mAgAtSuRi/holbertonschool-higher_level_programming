#!/usr/bin/python3

"""
prints name and first name
first_name: first name to print
last_name: last_name to print
"""


def say_my_name(first_name, last_name=""):
    """
    prints first name and name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    if last_name:
        print(f"My name is {first_name} {last_name}")
    else:
        print(f"My name is {first_name}")
