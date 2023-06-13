#!/usr/bin/python3

""" Modules to be imported """
import sys
import json


def save_to_json_file(my_obj, filename):
    """ Serialized an object to its JSON representation and writes it
    to a text file

    Args:
        my_obj: Object to be serialized
        filename: Path the file where the object would be written
    """
    with open(filename, mode='w', encoding="UTF8") as f:
        f.write(json.dumps(my_obj))


def load_from_json_file(filename):
    """ Deserializing a JSON file and creating an object

    Args:
        filename: path to the file where the objects would be created from

    Return: objects created
    """
    with open(filename, encoding="UTF8") as f:
        my_data = json.load(f)
    return my_data


def main():
    """ getting the command line arguments excluding script name """
    args = sys.argv[1:]

    """ list the hold all arguments """
    my_list = []

    my_list.extend(args)

    """ saving to required filename """
    save_to_json_file(my_list, "add_item.json")


if __name__ = "__main__":
    main()
