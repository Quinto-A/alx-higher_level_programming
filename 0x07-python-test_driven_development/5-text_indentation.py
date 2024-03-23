#!/usr/bin/python3
""" defines a function that prints a text with 2 new lines after each of the characters: ., ?, and :"""

def text_indentation(text):
    """a function that prints new lines after given characters.
    Args:
        text (int): the string from which the characters are determined.
    Raises: TypeError if ”text” is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end=" ")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in".?:":
                print("\n")
            c += 1
    while c < len(text) and text[c] == '':
        c += 1
    continue
    c += 1

