#!/usr/bin/python3
"""Defines a function"""


def is_same_class(obj, a_class):
    """determines if an object is a class instance
    Args:
        obj(): object to be determined
        a_class(): class being checked against
    """
    if isinstance(obj, a_class):
        return True
    #else:
    #    return False
