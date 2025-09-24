#!/usr/bin/python3
from abc import ABC, abstractmethod
import math
"""
Module to understand duck typing.
"""

class Shape(ABC):
	@abstractmethod
	def area(self):
		pass

	def perimeter(self):
		pass


class Circle(Shape):
	def __init__(self, radius):
		self.radius = radius

	def area(self):
		return math.pi * self.radius ** 2
	
	def perimeter(self):
		return 2 * math.pi * self.radius
	

class Rectangle(Shape):
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def area(self):
		return self.width * self.height
	
	def perimeter(self):
		return 2 * self.width + 2 * self.height
	
def shape_info(arg):
	print(arg.area())
	print(arg.perimeter())

circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=7)

shape_info(circle)
shape_info(rectangle)