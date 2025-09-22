#!/usr/bin/python3
"""
module checking  if the object is an instance of a class that inherited
(directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """returns true if the object is an instance of a_class that inherited
    directly from the class,
    otherwise False
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
