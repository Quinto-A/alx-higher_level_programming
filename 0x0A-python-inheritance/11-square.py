#!/usr/bin/python3
"""Defines a class square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """defines a square using Rectangle"""
    def __init__(self, size):
        """Initializes a new square"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns area of new square"""
        return self.__size * self.__size

    def __str__(self):
        """"Returns Rectangle description"""
        return f"[Square] {self.__size}/{self.__size}"
