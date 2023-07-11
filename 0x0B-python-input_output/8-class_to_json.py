#!/usr/bin/python3
"""class to json"""


def class_to_json(obj):
    """class to json

    Args:
        obj (any): convert obj to json dictionary

    Returns:
        dict: returns a dictionary
    """
    return obj.__dict__