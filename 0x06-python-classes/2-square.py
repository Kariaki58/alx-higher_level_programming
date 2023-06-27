#!/usr/bin/python3
"""create a class for square"""


class Square:
    """
    private instance attribute size
    """
    def __init__(self, size=0):
        self.__self = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
