#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    return {key: value * 2 for key, value in a_dictionary.items()}
    # new_dic = {}
    # for key, value in a_dictionary.items():
    #     new_dic[key] = value * 2
    # return new_dic
