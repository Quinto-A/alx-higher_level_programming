#!/usr/bin/python3
"""creates an object from JSON file"""


import json


def load_from_json_file(filename):
    """creates an object from JSON file"""
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)
