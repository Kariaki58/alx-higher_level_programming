#!/usr/bin/python3
"""student class"""


class Student:
    """instance atributes
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """
    convert to json
    """
    def to_json(self, attrs=None):
        if type(attrs) is list:
            for data in attrs:
                if not isinstance(data, str):
                    continue
                data = {d: getattr(self, d) for d in attrs if hasattr(self, d)}
                return data
        return self.__dict__
