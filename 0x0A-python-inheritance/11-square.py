#!/usr/bin/python3

"""square number one"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a class Square that inherits from Rectangle (9-rectangle.py)"""

    def __init__(self, size):
        """initialization function"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
