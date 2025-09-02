#!/usr/bin/python3


def uppercase(str):
    upp_str = ""
    for c in str:
        if ord(c) > 96 and ord(c) < 123:
            upper_ASCII = ord(c) - 32
            upp_str += chr(upper_ASCII)
        else:
            upp_str += c
    print("{}".format(upp_str))
