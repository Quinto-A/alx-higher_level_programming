#!/usr/bin/python3
"""Defines a module that reads a textfile"""


def read_file(filename=""):
    """reads a textfile and prints it to the stdout"""
    with open(filename, "r", encoding= "utf-8") as file:
        for line in file:
            print(line, end='')
