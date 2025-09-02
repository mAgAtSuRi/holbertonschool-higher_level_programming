#!/usr/bin/python3


def remove_char_at(str, n):
    count = 0
    new_str = ""
    for c in str:
        if count == n:
            continue
        new_str += c
    return new_str
