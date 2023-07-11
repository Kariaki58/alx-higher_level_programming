#!/usr/bin/python3
"""save to json file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file using JSON

    Args:
        my_obj (object): object input
        filename (string): file name
    """
    with open(filename, mode="w", encoding="UTF8") as file:
        file.write(json.dumps(my_obj))
