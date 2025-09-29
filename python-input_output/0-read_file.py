#!/usr/bin/python3

"""
Module to read a file
"""


def read_file(filename=""):
    """Function reading a file"""
    with open(filename) as f:
        print(f.read())
