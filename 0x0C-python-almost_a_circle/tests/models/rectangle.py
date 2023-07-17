#!/usr/bin/python3
from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    def __str__(self):
        m = "[Rectangle] ({}) {}/{} - {}/{}"
        return m.format(self.id, self.x, self.y, self.width, self.height)
    
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError("width must be an integer")
        
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("height must be an integer")
        
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x):
        if type(x) != int:
            raise TypeError("x must be an integer")
        
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, y):
        if type(y) != int:
            raise TypeError("y must be an integer")
        
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        return self.__height * self.__width
    
    def display(self):
        rectangle = []

        print("\n" * (self.__y), end="")
        for _ in range(self.__height):
            rectangle.append(" " * self.__x)
            rectangle.append("#" * self.__width)
            rectangle.append('\n')
        print("".join(rectangle), end="")
