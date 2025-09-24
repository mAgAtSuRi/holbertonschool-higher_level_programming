#!/usr/bin/python3
"""
Module demonstrating the use of abstract classes in Python
with the `abc` module.

This module defines an abstract class `Animal` and two concrete
implementations: `Dog` and `Cat`.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract class representing an animal.

    Any subclass must implement the `sound()` method.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by every subclass.

        Returns:
            str: the sound produced by the animal.
        """
        pass


class Dog(Animal):
    """
    Concrete class representing a dog.
    Inherits from `Animal` and implements the `sound()` method.
    """

    def sound(self):
        """
        Return the sound made by a dog.

        Returns:
            str: "Bark"
        """
        return "Bark"


class Cat(Animal):
    """
    Concrete class representing a cat.
    Inherits from `Animal` and implements the `sound()` method.
    """

    def sound(self):
        """
        Return the sound made by a cat.

        Returns:
            str: "Meow"
        """
        return "Meow"
