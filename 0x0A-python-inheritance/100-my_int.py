#!/usr/bin/python3
"""defines a class that inherits from int"""


class MyInt(int):
    """a class that iherits from int and inverts == and !="""

    def __eq__(self, other):
        """overide =="""
        return super().__ne__(other)

    def __ne__(self, other):
        """override !="""
        return super().__eq__(other)
