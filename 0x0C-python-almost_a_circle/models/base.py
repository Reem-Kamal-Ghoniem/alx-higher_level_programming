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
