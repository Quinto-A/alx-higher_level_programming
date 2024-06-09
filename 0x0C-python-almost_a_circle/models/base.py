#!/usr/bin/python3
""""a class named base"""


class Base:
    """ forms the base for all other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """creates a new class instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
