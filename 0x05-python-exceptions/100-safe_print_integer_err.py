#!/usr/bin/python3
# This function prints an integer
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return True

    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return False
