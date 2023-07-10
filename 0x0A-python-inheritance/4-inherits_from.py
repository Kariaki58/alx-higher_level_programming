#!/usr/bin/python3
"""inherits from a class
"""


def inherits_from(obj, a_class):
    """return true or false"""
    if type(obj) is not a_class and isinstance(obj, a_class):
        return True
    return False