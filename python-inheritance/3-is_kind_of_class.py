#!/usr/bin/python3
"""
module checking if an object is from a class or inheritate from the class
"""


def is_same_class(obj, a_class):
    """ "
    returns true if the object is an instance of a_class that inherited from,
    otherwise False
    """
    return isinstance(obj, a_class)
