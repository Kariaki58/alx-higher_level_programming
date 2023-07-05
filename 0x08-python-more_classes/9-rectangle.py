#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        dev_rect = ""
        for i in range(self.__height):
            dev_rect += str(self.print_symbol) * self.__width
            if i < self.__height - 1:
                dev_rect += "\n"
        return dev_rect

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def __repr__(self):
        string = "Rectangle(" + str(self.__width)
        string += ", " + str(self.__height) + ")"
        return string

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """returns the area of rectangle"""
    def area(self):
        return self.__width * self.__height

    """find and return the perimeter of Rectangle"""
    def perimeter(self):
        return 2 * (self.__height + self.__width)

    """returns the biggest rectangle based onn the area"""
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        cls.__width = size
        cls.__height = size
        new_rect = Rectangle(cls.__width, cls.__height)
        return new_rect
