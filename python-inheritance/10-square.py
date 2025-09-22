#!/usr/bin/python3
"""
Module square

Defines a Square class that inherits from Rectangle.
"""

Rectangle = __import__("9-rectangle.py").Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.

    Attributes:
        __size (int): size of the square (private)

    Methods:
        __init__(size): initializes the square and validates size.
        area(): returns the area of the square.
    """

    def __init__(self, size):
        """
        Initialize a Square instance.

        Args:
            size (int): size of the square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size <= 0
        """
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """
        Compute and return the area of the square.

        Returns:
            int: area of the square
        """
        return self.__size ** 2
