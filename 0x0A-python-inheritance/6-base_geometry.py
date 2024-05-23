#!/usr/bin/python3
"""Defines a class"""


class BaseGeometry:
    """defines a base geometry class"""

    def area(self):
        """Calculatea area of geometry"""
        raise NotImplementedError("area() is not implemented")
