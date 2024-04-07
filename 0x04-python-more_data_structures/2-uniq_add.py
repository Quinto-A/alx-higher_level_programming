#!/usr/bin/python3

def uniq_add(my_list=[]):
    totals = 0
    for i in set(my_list):
        totals += i
    return (totals)
