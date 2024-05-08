#!/usr/bin/python3
"""Define a class rectangle"""


class Rectangle:
    """Represents a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes a new rectangle
        Args:
          width(int): size of the rectangle.
        """
        self._width = width
        self._height = height

        @property
        def width(self):
            """Get/set the width of the rectangle"""
            return (self._width)

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            self._width = value

        @property
        def height(self):
            """Get/set the rectangle height"""
            return (self._height)

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
            self._height = value
