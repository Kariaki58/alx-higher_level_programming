#!/usr/bin/python3
"""
say_my_name: log out my name to stdout
"""


def say_my_name(first_name, last_name=""):
    """print out my name
    Args:
        first_name (str): get the first name
        last_name (str, optional): get the last name. Defaults to "".

    Raises:
        TypeError: if a wrong input is given
    """
    message = "first_name must be a string"
    message2 = "last_name must be a string"
    if (first_name is None):
        raise TypeError("missing argument")
    if not isinstance(first_name, str):
        raise TypeError(message)
    if not isinstance(last_name, str):
        raise TypeError(message2)
    print("My name is {} {}".format(first_name, last_name))
