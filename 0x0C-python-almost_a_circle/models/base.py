#!/usr/bin/python3
"""a module contains calss named base"""
import json
import csv
import os.path


class Base:
    """the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """the Initializes instances """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """changing list List to JSON string """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, mode='w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                json_string = cls.to_json_string(list_dicts)
                file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of dictionaries
        from the JSON string representation"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)
