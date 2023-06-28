#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """a function that replaces all occurrences of
    an element by another in a new list"""
    if not my_list:
        return my_list
    my_list = list(map(lambda x: x.replace(search, replace), str(my_list)))
    return my_list
