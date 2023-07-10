#!/usr/bin/python3

"""lookup function returns a list of directorys
"""
def lookup(obj):
    """function that returns a list of directorys

    Args:
        obj (object): get a object from main

    Returns:
        obj: return a list of directories
    """
    return dir(obj)