#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """a function that computes the square
    value of all integers of a matrix"""
    if not matrix:
        return None
    new_matrix = []
    for i in range len(matrix):
        new_matrix[i] = list(map(lambda x: x ** 2, matrix[i]))
    return (new_matrix)
