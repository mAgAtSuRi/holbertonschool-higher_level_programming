#!/usr/bin/python3


def roman_to_int(roman_string):
    if type(roman_string) is not str or not roman_string:
        return 0
    roman_dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    for letter in roman_string:
        result += roman_dic[letter]
    return result
