#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortedkeys = sorted(a_dictionary.keys())
    for key in sortedkeys:
        print("{}: {}".format(key, a_dictionary[key]))
