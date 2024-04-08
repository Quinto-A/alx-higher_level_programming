#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        sorted_items = max(a_dictionary, key=a_dictionary.get)
        return (sorted_items)
    else:
        return (None)
