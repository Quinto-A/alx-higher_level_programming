#!/usr/bin/python3
"""Defines a class"""


class BaseGeometry:
    """defines a base geometry class"""

    def area(self):
        """Calculatea area of geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if name is None or value is None:
            raise ValueError("empty argument list")
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
