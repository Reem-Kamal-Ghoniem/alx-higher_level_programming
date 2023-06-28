#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """a function that deletes keys with a specific value in a dictionary."""
    for key, value1 in a_dictionary.items():
        if value1 == value:
            del a_dictionary[key]
    return (a_dictionary)
