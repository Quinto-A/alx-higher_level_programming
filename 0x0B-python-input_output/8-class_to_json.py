#!/usr/bin/python3
"""a function that returns the dictionary description"""


def class_to_json(obj):
    """retunrs the dictionary description"""
    return obj.__dict__
