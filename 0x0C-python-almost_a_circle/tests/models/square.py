#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
    
    def __str__(self):
        m = "[Square] ({}) {}/{} - {}"
        return m.format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, x):
        self.width = x
        self.height = x
    
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
    
    def to_dictionary(self):
        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
    