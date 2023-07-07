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
    state = False
    while i < len(text):

        if text[i - 1] == "." or text[i - 1] == "?" or \
                text[i - 1] == ":" and i != 0:
            if text[i] == " ":
                state = True

            print("\n")
        else:
            state = False
        if not state:
            print(text[i], end="")
        i += 1
