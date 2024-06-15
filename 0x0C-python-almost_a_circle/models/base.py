#!/usr/bin/python3
""""a class named base"""

import json


class Base:
    """ forms the base for all other classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """creates a new class instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = f"{cls.__name__}.json"
        list_dicts = [obj.to_dictionary() for obj in list_objs] \
            if list_objs else []
        json_string = cls.to_json_string(list_dicts)
        with open(filename, "w") as file:
            file.write(json_string)
