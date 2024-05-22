#!/usr/bin/python3
"""Defines a class obj"""


def lookup(obj):
    """A function that returns the list of available attributes and methods
    Args:
        obj(object): object whose attributes and methods is to be determined
    Returns:
        list: A list representing the names of the attributes and methods
    """

    return dir(obj)
