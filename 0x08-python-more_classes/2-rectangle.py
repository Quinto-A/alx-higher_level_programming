#!/usr/bin/python3
"""Defines a class rectangle"""


class Rectangle:
    """Defines a rectangle"""
    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height

    @property
    def width(self):
        """Get/set width of the rectangle"""
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("wdth must be >= 0")
        self._width = value
