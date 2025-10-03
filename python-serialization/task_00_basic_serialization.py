#!/usr/bin/python3
import json

"""Module to serialize and deserialize"""


def serialize_and_save_to_file(data, filename):
    """serialize data in filename"""
    json.dump(data, filename)


def load_and_deserialize(filename):
    """deserialize data from filenam and return it"""
    return json.load(filename)
