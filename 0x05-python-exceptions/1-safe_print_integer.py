#!/usr/bin/python3
# This function prints integer from a list
def safe_print_integer(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
        else:
            return False
    except ValueError:
        pass
