#!/usr/bin/python3
"""Script that sends a URL request and displays the value of a variable
in the header
Modules to be used to be used
"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        print(headers.get("X-Request-Id"))
