#!/usr/bin/python3
"""check if it is same class
"""


def is_same_class(obj, a_class):
    """is same class?

    Args:
        obj (type): data type
        a_class (a_class): compare two objects
    Returns:
        bool: True/false
    """
    if type(obj) is a_class:
        return True
    return False
