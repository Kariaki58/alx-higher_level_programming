#!/usr/bin/python3
from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        
        if x < 0:
            raise ValueError("x must be > 0")
        self.__x = x
    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("{} must be an integer".format(y))
        
        if y < 0:
            raise ValueError("{} must be > 0".format(y))
        self.__y = y