#!/usr/bin/python3
"""Defines a class square"""

class Square:
    """Represent a square"""

    def __init__(self, size):
    """Initializes a new squar
Args:
      size(int): The size of the new square
    """

    self.size  = size

    @property
    def size(self):
      """get the current square size"""
      return(self.__size)

    @size.setter
    def size(self, value):
      if not isinstance(value, int):
        raise TypeError("size must be an integer")
      elif value < 0:
        raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
      """Return the current area of the square"""
      return(self.__size * self.__size)

    def print(self):
      """Print the square with the # character"""
    for i in range(0, self.__size):
          [print("#", end="") for j in range(self.__size)]
          print("")
