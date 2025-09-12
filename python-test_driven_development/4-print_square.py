#!/usr/bin/python3
"""
prints a square made of #
size: size of the square
"""


def print_square(size):
    if type(size) is not int or (type(size) is float and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError(("size must be >= 0"))
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()

print_square(2.5)
print("")
print_square(10)
print("")
print_square(0)
print("")
print_square(1)
print("")
try:
    print_square(-1)
except Exception as e:
    print(e)
print("")