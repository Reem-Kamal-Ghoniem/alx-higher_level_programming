#!/usr/bin/python3
"""a module that contains the square class
which is a special case of rectangles"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """the clas of the square"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialization function"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """describing the square as a string"""
        _square = "[Square] "
        _id = "({}) ".format(self.id)
        _xy = "{}/{} - ".format(self.x, self.y)
        _wh = "{}/{}".format(self.width)

        return _square + _id + _xy + _wh

    @property
    def size(self):
        """getter for the size"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updating the square"""
        if args and len(args) is not 0:
            attr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if attr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, attr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """representing the square as a dictionary"""
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
