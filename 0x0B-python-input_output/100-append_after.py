#!/usr/bin/python3
"""Insert a line of to a file text """


def append_after(filename="", search_string="", new_string=""):
    """insert line of text to a file"""
    with open(filename, mode='r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(filename, 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string + '\n')
