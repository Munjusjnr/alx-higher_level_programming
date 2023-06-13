#!/usr/bin/python3

""" Modules to be imported """
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def argument_to_list(args):
    """ getting the command line arguments excluding script name """
    args = sys.argv[1:]
    try:
        my_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        my_list = []

    my_list.extend(args)

    """ saving to required filename """
    save_to_json_file(my_list, "add_item.json")
