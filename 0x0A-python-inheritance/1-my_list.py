#!/usr/bin/python3
"""Defines a class that inherits from list"""


class MyList(list):
    """Defines a module that sorts a list"""

    def print_sorted(self):
        """"prints a list in ascending order"""
        print(sorted(self))
