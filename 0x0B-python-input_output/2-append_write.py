#!/usr/bin/python3
"""append to a file"""


def append_write(filename="", text=""):
    char_len = 0

    with open(filename, mode="a", encoding="UTF8") as file:
        for data in text:
            file.writelines(data)
            char_len += 1
    return char_len
