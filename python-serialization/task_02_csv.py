#!/usr/bin/python3
import csv
import json

"""Module to convert csv to json"""


def convert_csv_to_json(csv_filename):
    """convert csv filename to json"""
    try:
        with open(csv_filename) as f:
            csv_reader = csv.DictReader(f)
            try:
                with open("data.json", "w") as fjson:
                    json.dump(list(csv_reader), fjson)
                return True
            except Exception:
                return False
    except Exception:
        return False
