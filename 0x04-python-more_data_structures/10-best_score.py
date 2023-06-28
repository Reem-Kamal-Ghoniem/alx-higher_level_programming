#!/usr/bin/python3
def best_score(a_dictionary):
    """a function that returns a key with the biggest integer value."""
    if not a_dictionary:
        return None

    max_value = 0
    max_key = ""
    for key, value in a_dictionary.items():
        if value > max_value:
            max_key = key
    return max_key
