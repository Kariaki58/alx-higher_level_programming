#!/usr/bin/python3
"""from json string"""
import json


def from_json_string(my_str):
    """convert from json format to string

    Args:
        my_str (str): object

    Returns:
        json: object
    """
    return json.loads(my_str)
