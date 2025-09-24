#!/usr/bin/python3
"""
Module to demonstrate abstract classes and duck typing in Python.

This module defines an abstract base class `Shape` and two concrete
implementations: `Circle` and `Rectangle`. It also provides a helper
function `shape_info()` that prints the area and perimeter of any
object that implements these methods (duck typing).
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class representing a geometric shape.

    Subclasses must implement:
        - area()
        - perimeter()
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to compute the area of the shape.

        Returns:
            float: the computed area.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to compute the perimeter of the shape.

        Returns:
            float: the computed perimeter.
        """
        pass


class Circle(Shape):
    """
    Concrete class representing a circle.
    """

    def __init__(self, radius):
        """
        Initialize a Circle instance.

        Args:
            radius (float): the radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Compute the area of the circle.

        Returns:
            float: area of the circle.
        """
        return abs(math.pi * self.radius ** 2)

    def perimeter(self):
        """
        Compute the perimeter (circumference) of the circle.

        Returns:
            float: perimeter of the circle.
        """
        return abs(2 * math.pi * self.radius)


class Rectangle(Shape):
    """
    Concrete class representing a rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance.

        Args:
            width (float): the width of the rectangle.
            height (float): the height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Compute the area of the rectangle.

        Returns:
            float: area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Compute the perimeter of the rectangle.

        Returns:
            float: perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(arg):
    """
    Print the area and perimeter of any object that implements
    `area()` and `perimeter()` methods.

    This demonstrates duck typing: the function does not check
    the type of the object, only that it has the required methods.

    Args:
        arg (object): Any object with `area()` and `perimeter()` methods.
    """
    print(f"Area: {arg.area()}")
    print(f"Perimeter: {arg.perimeter()}")
    
circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=7)

shape_info(circle)
shape_info(rectangle)
