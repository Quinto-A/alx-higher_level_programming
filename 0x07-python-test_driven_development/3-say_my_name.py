#!/usr/bin/python3
"""This is a module that defines a function that prints a name"""

def say_my_name(first_name, last_name=""):
    """Printss My name is <first name> <last name>
    Args:
        first_name (str): first name to be printed
        last_name (str): last name to be printed
    Raise:
        TypeError: If either first_name or last_name are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

