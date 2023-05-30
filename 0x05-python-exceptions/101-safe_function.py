#!/usr/bin/python3
# This function executes a function safely
def safe_function(fct, *args):
    import sys
    try:
        res = fct(*args)
        return res
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return None
