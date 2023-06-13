#!/usr/bin/python3

""" Modules to be imported """
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def argument_to_list(args):
    """ Add command-line arguments to list and save to JSON file

        Arguments:
            args: command-line arguments
    """
    try:
        my_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        my_list = []

    my_list.extend(args)

    """ saving to required filename """
    save_to_json_file(my_list, "add_item.json")


""" command-line arguments without script name """
args = sys.argv[1:]

""" adding arguments to list and saving to JSON File """
argument_to_list(args)
