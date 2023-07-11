#!/usr/bin/python3

"""file that wil Improve Geometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """representing a rectangle"""

    def __init__(self, width, height):
        """define w, h"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
