#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sort_dic = list(sorted(a_dictionary))
    for key in sort_dic:
        print(key, ":", a_dictionary[key])
