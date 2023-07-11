#!/usr/bin/python3

"""Same class or inherit from"""


def is_kind_of_class(obj, a_class):
    """a function that returns True if the object is
    exactly an instance of the specified class

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
