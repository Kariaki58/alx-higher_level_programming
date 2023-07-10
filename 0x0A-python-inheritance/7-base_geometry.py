#!/usr/bin/python3
"""add more fuctionality"""


class BaseGeometry:
    """area not implemented"""
    def area(self):
        raise Exception("area() is not implemented")
    
    """integer_validator"""
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
