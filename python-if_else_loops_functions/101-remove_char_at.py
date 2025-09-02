#!/usr/bin/python3


def remove_char_at(str, n):
    count = 0
    new_str = ""
    for c in str:
        if count == n:
            count += 1
            continue
        new_str += c
        count += 1
    return new_str


print(remove_char_at("012345", 1))