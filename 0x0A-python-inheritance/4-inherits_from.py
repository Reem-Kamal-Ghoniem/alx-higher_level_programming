#!/usr/bin/python3

"""a function that returns True if the object is an instance of a class"""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        true or false
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
