#!/usr/bin/python3
"""MyList class
"""

class MyList(list):
    """class that inherits from list class

    Args:
        list (list): inherties from list
    """
    def print_sorted(self):
        """
        print sorted list
        """
        print(sorted(self))