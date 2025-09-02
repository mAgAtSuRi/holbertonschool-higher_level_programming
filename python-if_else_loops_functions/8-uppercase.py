#!/usr/bin/python3


def uppercase(str):
    for c in str:
        if ord(c) > 96 and ord(c) < 123:
            upper_ASCII = ord(c) - 32
            print(chr(upper_ASCII), end="")
        else:
            print(c, end="")
