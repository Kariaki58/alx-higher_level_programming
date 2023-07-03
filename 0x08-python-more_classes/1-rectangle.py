#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:
    """object to set the width and height of the rectangle"""
    
    def __init__(self, width=0, height=0):
        """set a new Rectangle.
        Args:
            width(int): The width of rectangle
            height(int): the height of rectangle.
        """
        self.__height = height
        self.__width = width

    """width property class"""
    @property
    def width(self):
        return self.__width

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
        return self.__height

    """setter method for height"""
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value
