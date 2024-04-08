#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        sorted_items = sorted(a_dictionary.items(), key=lambda x: x[1])
        return (sorted_items[-1])
    else:
        return (None)
