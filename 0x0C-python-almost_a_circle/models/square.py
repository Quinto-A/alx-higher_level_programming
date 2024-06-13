#!/usr/bin/python3
"""a class square that inherits from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """Overrides the __str__method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - " \
               f"{self.width}/{self.height}"
