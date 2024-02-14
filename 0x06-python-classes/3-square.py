#!/bin/python3

"""Define a class square"""


class Square:
    """Represents a square"""

    def __init__(self, size):
        """Initializes a new square.

        Args:
            size (int): new square size
        """

        if not instance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return area of current square"""

        return (self.__size * self.__size)
