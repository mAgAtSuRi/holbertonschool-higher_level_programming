#!/usr/bin/python3

"""Module to write content in a file"""


def write_file(filename="", text=""):
    """Functionwrite in filename and returning the number of bytes written"""
    with open(filename, "w") as f:
        return f.write(text)
