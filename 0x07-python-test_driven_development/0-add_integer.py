#!/usr/bin/python3
"""
add_integer: add two integer
Args:
    a(int): input integer value a
"""


def add_integer(a, b=98):
    """function that return the addition of a and b
    b(int, optional): integer value b. Dfaults to 98
    """
    m = "add_integer() missing 1 required positional argumnet: 'a'"
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    if a is None:
        raise TypeError(m)
    return (a + b)
