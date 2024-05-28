#!/usr/bin/python3
"""writes object to text file using JSON"""

import json


def save_to_json_file(my_obj, filename):
    """writes object to text file using JSON"""
    with open(filename, mode='a', encoding='utf-8') as file:
        return json.dump(my_obj, file)
