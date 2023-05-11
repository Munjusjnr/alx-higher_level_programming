#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    if length == 1:
        print("0 arguments.")
    else:
        print("{:d} argument{}:".format(length - 1, '' if length == 2
              else 's'))
        for i in range(1, length):
            print("{:d}: {:s}".format(i, sys.argv[i]))
