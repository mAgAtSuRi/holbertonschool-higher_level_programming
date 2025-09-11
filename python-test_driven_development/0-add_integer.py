#!/usr/bin/python3
"""
Adds 2 integers and check if its doable
"""


def add_integer(a, b=98):
    """
    Adds two numbers after checking if they are integers or floats.
    Floats are converted to integers before addition.

    Args:
        a: first number (int or float)
        b: second number (int or float, default=98)

    Returns:
        int: sum of a and b

    Raises:
        TypeError: if a or b are not int or float
        OverflowError: if a or b is too large to convert to int
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    try:
        return int(a) + int(b)
    except OverflowError:
        raise OverflowError("number too large to convert to integer")
