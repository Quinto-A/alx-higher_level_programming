#!/usr/bin/python3
"""Defines a function"""


def is_kind_of_class(obj, a_class):
    """eturns True if the object is an instance of a class or inherited class
    Args:
        obj(): object being checked
        a_class(): class it is being checked against
    """
    def is_kind_of_class(obj, a_class):
        if isinstance(obj, a_class):
            return True
