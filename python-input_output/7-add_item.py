#!/usr/bin/python3

"""Module to load add and save with json"""
import sys
import os

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

if os.path.exists("add_item.json"):
    arg_list = load_from_json_file("add_item.json")
else:
    arg_list = []

for i in range(1, len(sys.argv)):
    arg_list.append(sys.argv[i])
# other technique:
# arg_list.extend(sys.argv[1:])

save_to_json_file(arg_list, "add_item.json")
