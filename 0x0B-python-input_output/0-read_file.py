#!/usr/bin/python3
"""read from a file
"""


def read_file(filename=""):
    """read from a text file(UTF-8) and prints it to stdout

    Args:
        filename (str, optional): get the file name. Defaults to "".
    """
    with open(filename, mode="r", encoding="UTF8") as f:
        print(f.read())
