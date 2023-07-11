#!/usr/bin/python3
"""a function that returns the list of available
attributes and methods of an object"""


def lookup(obj):
    """returns a list of objects"""
    return (dir(obj))
