#!/usr/bin/python3

"""class-checking function."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        true or false
    """
    if type(obj) == a_class:
        return True
    else:
        return False
