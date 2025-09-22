#!/usr/bin/python3
"""
Module geometry

This module defines a BaseGeometry class that serves as a base
for geometric shapes. It provides a placeholder method for area()
and a validator for integer attributes.
"""


class BaseGeometry:
    """
    BaseGeometry class for geometric shapes.

    Methods:
        area(): raises an Exception because area is not implemented.
        integer_validator(name, value): validates that value is a positive
        integer.
    """

    def area(self):
        """
        Computes the area of the geometric shape.

        Raises:
            Exception: always, since area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is a positive integer.

        Args:
            name (str): name of the parameter (used in exception messages)
            value (int): value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is <= 0
        """
        if type(value) is not int:
            raise TypeError(f"{value} must be an integer")
        if value <= 0:
            raise ValueError(f"{value} must be greater than 0")
