#!/usr/bin/python3
"""write a file using UTF8 encoding
"""


def write_file(filename="", text=""):
    """function that writes a string to a text file

    Args:
        filename (str, optional): file name. Defaults to "".
        text (str, optional): text data. Defaults to "".
    """
    char_num = 0

    with open(filename, mode="w", encoding="UTF8") as file:
        for data in text:
            file.write(data)
            char_num += 1
    return char_num
