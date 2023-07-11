#!/usr/bin/python3
"""append to a file"""


def append_write(filename="", text=""):
    """append to a file

    Args:
        filename (str, optional): file name input. Defaults to "".
        text (str, optional): main text. Defaults to "".

    Returns:
        int: returnt the number of characters added
    """
    char_len = 0

    with open(filename, mode="a", encoding="UTF8") as file:
        for data in text:
            file.writelines(data)
            char_len += 1
    return char_len
