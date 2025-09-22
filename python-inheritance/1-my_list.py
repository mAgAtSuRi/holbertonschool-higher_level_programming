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

my_list = MyList()
my_list.append(2)
my_list.append(-1)
print(my_list)
my_list.print_sorted()