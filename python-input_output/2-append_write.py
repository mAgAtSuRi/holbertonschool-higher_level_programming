#!/usr/bin/python3

"""Module to append content"""


def append_write(filename="", text=""):
    """function to append text in filename"""
    with open(filename, "a") as f:
        return f.write(text)
