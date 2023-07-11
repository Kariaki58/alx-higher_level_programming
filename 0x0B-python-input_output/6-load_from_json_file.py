#!/usr/bin/python3
"""load from json"""
import json


def load_from_json_file(filename):
    """load from json file

    Args:
        filename (str): string object
    """
    with open(filename, "r", encoding="UTF8") as file:
        object = json.loads(file.read())
    return object
