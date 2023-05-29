#!/usr/bin/python3
# This function returns the division of two integers
def safe_print_division(a, b):
    result = None
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(result))
