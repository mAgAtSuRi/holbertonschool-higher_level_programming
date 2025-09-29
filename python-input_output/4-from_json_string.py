#!/usr/bin/python3

"""module returning an object representing by a JSON string"""
import json


def from_json_string(my_str):
    """function decoding json string"""
    return json.loads(my_str)
