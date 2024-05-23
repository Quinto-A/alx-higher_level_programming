#!/usr/bin/python3
"""Defines a function"""


def inherits_from(obj, a_class):
    """determines if an objected is instance of direct or indirect inheritance"""
    if any(issubclass(type(obj), subclass) for subclass in a_class.__subclasses__()):
        return True
