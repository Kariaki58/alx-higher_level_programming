#!/usr/bin/python3
import json


class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        return "[]" if list_dictionaries is None or \
            len(list_dictionaries) <= 0 else json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        list_datas = []

        if json_string is None:
            return list_datas
        
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        file_name = "{}.json".format(cls.__name__)
        storage_temp = []

        if list_objs is not None:
            for data in list_objs:
                data = data.to_dictionary()
                dict_data = cls.to_json_string(data)
                strings = json.loads(dict_data)
                storage_temp.append(strings)
        with open(file_name, mode="w", encoding="UTF8") as file:
            json.dump(storage_temp, file)


    @classmethod
    def create(cls, **dictionary):
        from models.rectangle import Rectangle
        from models.square import Square

        if (cls.__name__ == "Rectangle"):
            dummy_inst = Rectangle(2, 3)
        
        if (cls.__name__ == "Square"):
            dummy_inst = Square(4)
        
        dummy_inst.update(**dictionary)
        return dummy_inst
    
    @classmethod
    def load_from_file(cls):
        from models.rectangle import Rectangle
        from models.square import Square

        filename = "{}.json".format(cls.__name__)
        list_content = []

        if cls.__name__ == "Rectangle":
            r1 = Rectangle(2, 3)
            try:
                with open(filename, mode="r", encoding="UTF8") as load:
                    for content in load:
                        data = cls.from_json_string(content)
                        to_dict = data.to_dictionary()
                        r1.create(to_dict)
            except:
                return list_content
        
        elif cls.__name__ == "Square":
            r2 = Square(5)

            try:
                with open(filename, mode="r", encoding="UTF8") as load:
                    for content in load:
                        data = cls.from_json_string(content)
                        to_dict = data.to_dictionary()
                        r2.create(to_dict)