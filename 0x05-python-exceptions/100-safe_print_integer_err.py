#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    """ prints an integer.

    Args:
        Value (int): integer to be printed.

    Returns:
        True if value has been correctly printed
    """
    try:
        print("{:d}".format(value))
        return (True)
    except(TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
