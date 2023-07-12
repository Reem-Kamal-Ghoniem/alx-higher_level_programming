#!/usr/bin/python3

"""a file that defines the function load_from_json_file"""
import json


def load_from_json_file(filename):
    """a function that creates an Object from a “JSON file”"""
    with open(filename) as f:
        return json.load(f)
