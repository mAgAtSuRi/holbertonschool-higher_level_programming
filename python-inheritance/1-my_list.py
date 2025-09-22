#!/usr/bin/python3

"""
module that creates a class inherating
"""


class MyList(list):
    """
    class sorting a list
    """
    def print_sorted(self):
        print(sorted(self))
