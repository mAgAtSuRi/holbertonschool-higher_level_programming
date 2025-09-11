#!/usr/bin/python3
"""
Adds 2 integers and check if it's doable
"""


def add_integer(a, b=98):
    """
    Adds two integers a and b and returns the result
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
