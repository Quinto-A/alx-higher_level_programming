#!/usr/bin/python3

def no_c(my_string):
    fstring = ""
    for char in my_string:
        if char.lower() != 'c':
            fstring += char
    return fstring
