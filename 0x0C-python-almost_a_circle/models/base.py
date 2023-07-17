#!/usr/bin/python3
"""the Base class a.k.a the parent"""
import json
import csv


class Base:
    """class object
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """the instance of this class

        Args:
            id (int, optional): set the id to id. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        convert string to json
        """
        return "[]" if list_dictionaries is None or \
            len(list_dictionaries) <= 0 else json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """converts from json to string"""
        list_datas = []

        if json_string is None:
            return list_datas
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """save list objs to a file

        Args:
            list_objs (object): dump the data to file
        """
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
        """create a new instance with a constant type
        Returns:
            inst: dummy instance
        """
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
        """load a json data from a file

        Returns:
            list: list content
        """
        filename = "{}.json".format(cls.__name__)
        list_content = []

        try:
            with open(filename, mode='r', encoding="UTF8") as file:
                json_status = cls.from_json_string(file.read())
            for data in json_status:
                inst = cls.create(**data)
                list_content.append(inst)
            return list_content
        except Exception:
            return list_content
    
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save to csv file"""
        filename = "{}.csv".format(cls.__name__)

        with open(filename, mode="w", newline="", encoding="UTF8") as file:
            csv_status = csv.writer(file, delimiter=" ")

            if (cls.__name__ == "Rectangle"):
                for data in list_objs:
                    dictionary = data.to_dictionary()
                    str_text = "{}, {}, {}, {}, {}".format(
                        str(dictionary["id"]), str(dictionary["width"]),
                        str(dictionary["height"]), str(dictionary["x"]),
                        str(dictionary["y"]))
                    csv_status.writerow(str_text)

            if cls.__name__ == "Square":
                for data in list_objs:
                    dictionary = data.to_dictionary()
                    str_text = ""
                    str_text += "{}, {}, {}, {}".format(
                        str(dictionary["id"]), str(dictionary["size"]),
                        str(dictionary["x"]), str(dictionary["y"]))
                    csv_status.writerow(str_text)
    

    # try:
    #         with open(filename, mode='r', encoding="UTF8") as file:
    #             json_status = cls.from_json_string(file.read())
    #         for data in json_status:
    #             inst = cls.create(**data)
    #             list_content.append(inst)
    #         return list_content
    #     except Exception:
    #         return list_content
    
    @classmethod
    def load_from_file_csv(cls):
        """returns a list"""
        filename = "{}.csv".format(cls.__name__)

        try:
            with open(filename, mode="r", newline="", encoding="UTF8") as file:
                if cls.__name__ == "Rectangle":
                    
        except Exception:
            return []