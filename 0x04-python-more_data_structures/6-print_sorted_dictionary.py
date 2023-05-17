#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dictkeys = list(a_dictionary.keys())
    dictkeys.sort()
    sorteddict = {i: a_dictionary[i] for i in dictkeys}
    print(sorteddict)
