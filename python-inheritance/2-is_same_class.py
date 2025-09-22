#!/usr/bin/python3
"""
module checking if an object is from a class
"""


def is_same_class(obj, a_class):
    """ "
    returns true if the object is an instance of a_class otherwise False
    """
    return type(obj) is a_class
