#!/usr/bin/python3
"""Defines a class that inherits from list"""


class MyList(list):
    """Defines a module that sorts a list"""

    def print_sorted(self):
        if not self:
            raise ValueError("Cannot print sorted list: List is empty")

        print(sorted(self))
