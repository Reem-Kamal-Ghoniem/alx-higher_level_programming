#!/usr/bin/python3
"""a class Square that defines a square"""


class Square():
    """square class with it's size"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if (type(value) is not int):
            raise TypeError("value must be an integer")
        elif (value < 0):
            raise ValueError("value must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
