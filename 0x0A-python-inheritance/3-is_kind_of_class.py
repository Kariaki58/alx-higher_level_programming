#!/usr/bin/python3
"""is kind of a class
"""


def is_kind_of_class(obj, a_class):
    """return true if the obj match with a_class

    Args:
        obj (data type): get the data type
        a_class (unknow): in build type

    Returns:
        bool: True/False
    """
    if isinstance(obj, a_class):
        return True
    return False