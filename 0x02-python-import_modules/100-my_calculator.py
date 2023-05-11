#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif sys.argv[2]) not in ['+' or '-' or '*' or '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] == '+':
            print(f"{a} + {b} = {add(a, b)}")
        elif sys.argv[2] == '-':
            print(f"{a} - {b} = {sub(a, b)}")
        elif sys.argv[2] == '*':
            print(f"{a} * {b} = {mul(a, b)}")
        elif sys.argv[2] == '/':
            print(f"{a} / {b} = {div(a, b)}")
