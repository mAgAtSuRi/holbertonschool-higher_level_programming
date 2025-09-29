#!/usr/bin/python3

"""Module creating an object from json file"""
import json


def load_from_json_file(filename):
    """function that  creates an Object from a json file"""
    with open(filename) as f:
        return json.load(f)
