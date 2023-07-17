#!/usr/bin/python3
"""Square class

    Raises:
        ValueError: when you input wrongly

    Returns:
        any: returns any type
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """create the instance attribute

    Args:
        Rectangle (): inherites the recangle class with super()
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
    
    """returns the instance in string formate"""
    def __str__(self):
        m = "[Square] ({}) {}/{} - {}"
        return m.format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """returns the size as width"""
        return self.width

    @size.setter
    def size(self, x):
        self.width = x
        self.height = x
    
    """
    updates the function when called 
    accepts multiple arguments and also dictionaries
    """
    def update(self, *args, **kwargs):
        length = len(args)

        try:
            if (length > 0):
                raise ValueError
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return
        
        except ValueError:
            if (length == 1):
                self.id = args[0]
            elif (length == 2):
                self.id, self.size = args
            elif (length == 3):
                self.id, self.size, self.x = args
            elif (length == 4):
                self.id, self.size, self.x, self.y = args
    
    """convert instance to dictionary"""
    def to_dictionary(self):
        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
