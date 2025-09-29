#!/usr/bin/python3

"""
Module to read a file
"""


def read_file(filename=""):
    """Function reading a file"""
    with open(filename) as f:
        for line in f:
            print(line, end="")

read_file("my_file_0.txt")