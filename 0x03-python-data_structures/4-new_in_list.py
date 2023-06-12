#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """replaces an element"""
    if not my_list:
        pass
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
