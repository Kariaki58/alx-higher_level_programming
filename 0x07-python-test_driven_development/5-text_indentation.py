#!/usr/bin/python3
"""
text_indentation: indent if it sees . ? :
"""


def text_indentation(text):
    """prints a text with 2 new lines

    Args:
        text (str): always string

    Raises:
        TypeError: wrong input
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    new_string = ""
    while i < len(text):

        if text[i - 1] == "." or text[i - 1] == "?" or \
                text[i - 1] == ":" and i != 0:
            if text[i] == " ":
                new_string += "\n"
        else:
            new_string += text[i]
        i += 1
    print(new_string)