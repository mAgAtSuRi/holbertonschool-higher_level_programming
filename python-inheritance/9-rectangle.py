#!/usr/bin/python3
"""
Module rectangle

Defines a Rectangle class that inherits from BaseGeometry.
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.

    Attributes:
        __width (int): width of the rectangle (private)
        __height (int): height of the rectangle (private)

    Methods:
        __init__(width, height): initializes the rectangle and validates width
        and height.
        area(): returns the area of the rectangle.
        __str__(): returns a formatted string representation of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance.

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle

        Raises:
            TypeError: if width or height is not an integer
            ValueError: if width or height <= 0
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
