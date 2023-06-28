#!/usr/bin/python3
def best_score(a_dictionary):
    """a function that returns a key with the biggest integer value."""
    max = 0
    for key, value in a_dictionary.items():
        if value > max:
            max = value
    return max
