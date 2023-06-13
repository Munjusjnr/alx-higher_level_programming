#!/usr/bin/python3

""" Modules to be imported """
import sys
from 5-save_to_json_file.py import save_to_json_file
from 6-load_from_json_file.py import load_from_json_file


if __name__ = "__main__":
    """ getting the command line arguments including script name """
    args = sys.argv[1:]
    """ list the hold all arguments """
    my_list = []
    my_list.extend(args)
    """ saving to required filename """
    save_to_json_file(my_list, "add_item.json")
