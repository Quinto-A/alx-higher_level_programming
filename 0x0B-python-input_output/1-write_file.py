#!/usr/bin/python3
"""writes a string to a text file and returns character number"""


def write_file(filename="", text=""):
    """writes a string to a text file and returns character number"""
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(text)
