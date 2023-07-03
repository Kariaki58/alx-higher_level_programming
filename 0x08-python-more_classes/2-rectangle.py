#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    """width property class"""
    @property
    def width(self):
        return self.width

    """propety setter"""
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """height property class"""
    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            print("height must be >= 0")
        self.__height = value

    """return the area of the rectangle"""
    def area(self):
        return self.__height * self.__width

    """return the perimeter of the rectangle"""
    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)
