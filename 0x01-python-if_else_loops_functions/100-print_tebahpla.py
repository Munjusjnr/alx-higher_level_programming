#!/usr/bin/python3
for letters in range(ord('z'), ord('a') - 1, -1):
    print("{:c}".format(letters)if letters % 2 == 0
          else chr(letters - 32), end="")
