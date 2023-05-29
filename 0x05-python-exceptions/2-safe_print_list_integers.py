#!/usr/bin/python3
# This function prints the first x(integers) of a list
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for value in range(x):
            if isinstance(my_list[value], int):
                print("{:d}".format(my_list[value]), end="")
                count += 1
    except IndexError:
        pass

    print()
    return count
