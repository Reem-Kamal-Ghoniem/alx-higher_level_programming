#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """a function that computes the square
    value of all integers of a matrix"""
    if not matrix:
        return None
    new_matrix = []
    for i in range matrix:
        new_matrix[i] = matrix[i] ** 2
    return (new_matrix)
