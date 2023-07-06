#!/usr/bin/python3
class LockedClass:
    __slots__ = ('first_name',)

    def __setattr__(self, name, value):
        if not hasattr(self, 'first_name') and name != 'first_name':
            raise AttributeError("Cannot create new instance attributes")
        super().__setattr__(name, value)
