#!/usr/bin/python3
for numbers in range(0, 100):
    if numbers >= 0 and numbers < 99:
        print("{:02d}".format(numbers), end=", ")
    if numbers == 99:
        print("99")
