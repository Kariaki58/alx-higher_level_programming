#!/usr/bin/python3
"""the Base class a.k.a the parent"""
import json
import csv
import turtle


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
        """save to csv file

        Args:
            list_objs (inst):
        """
        filename = "{}.csv".format(cls.__name__)
        with open(filename, mode="w", newline="") as file:
            if cls.__name__ == "Rectangle":
                fields = ["id", "width", "height", "x", "y"]
            else:
                fields = ["id", "size", "x", "y"]
            writer = csv.DictWriter(file, fieldnames=fields)
            for data in list_objs:
                writer.writerow(data.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        load from file to csv
        """
        filename = "{}.csv".format(cls.__name__)
        store = []
        try:
            with open(filename, mode="r", newline="") as file:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                reader = csv.DictReader(file, fieldnames=fields)
                for data in reader:
                    for key, val in data.items():
                        data[key] = int(val)
                    store.append(cls.create(**data))
            return store
        except Exception:
            return store

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draw rectangle and square in the screen

        Args:
            list_rectangles (object):
            list_squares (object):
        """
        screen = turtle.Screen()
        screen.bgcolor('#212623')
        rect_move = turtle.Turtle()
        rect_move.color('green')
        rect_move.pen(pensize=4)
        for objects in list_rectangles:
            rect_move.penup()
            rect_move.goto(objects.x, objects.y)
            rect_move.pendown()
            rect_move.forward(objects.width)
            rect_move.right(90)
            rect_move.forward(objects.height)
            rect_move.right(90)
            rect_move.forward(objects.width)
            rect_move.right(90)
            rect_move.forward(objects.height)
            rect_move.hideturtle()
        for objects in list_squares:
            rect_move.penup()
            rect_move.goto(objects.x, objects.y)
            rect_move.pendown()
            rect_move.forward(objects.size)
            rect_move.right(90)
            rect_move.forward(objects.size)
            rect_move.right(90)
            rect_move.forward(objects.size)
            rect_move.right(90)
            rect_move.forward(objects.size)
        print(rect_move.position())
        turtle.exitonclick()
