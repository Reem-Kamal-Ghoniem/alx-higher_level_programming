#!/usr/bin/python3

"""a file that defines function called save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """a function that writes an Object to a text file,
    using a JSON representation"""
    with open(filename, "w") as f:
        return json.dump(my_obj, f)
