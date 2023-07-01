#!/usr/bin/python3
"""write a class Square that defines a square"""


class Square:
    """drawing a square in the terminal"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        print("here")
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            length = int(self.area() / self.__size)
            for i in range(length):
                for j in range(length):
                    print("#", end="")
                print()
