#!/usr/bin/python3
import json

"""Module to serialize and deserialize"""


def serialize_and_save_to_file(data, filename):
    """serialize data in filename"""
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """deserialize data from filenam and return it"""
    with open(filename) as f:
        return json.load(f)
    