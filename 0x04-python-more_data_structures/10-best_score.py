#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        sorted_items = sorted(a_dictionary.items())
        v = sorted_items[-1]
        return (v)
    else:
        return (None)
