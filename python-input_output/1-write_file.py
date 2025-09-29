#!/usr/bin/python3

"""Module to write content in a file"""


def write_file(filename="", text=""):
    with open(filename, "w") as f:
        return f.write(text)
