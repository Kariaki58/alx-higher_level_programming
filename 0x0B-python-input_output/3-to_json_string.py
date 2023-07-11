#!/usr/bin/python3
"""get the json representation of an object(string)"""
import json


def to_json_string(my_obj):
    """convert an object to json and return it

    Args:
        my_obj (any): return json.my_obj
    """
    to_json = json.dumps(my_obj)
    return to_json
