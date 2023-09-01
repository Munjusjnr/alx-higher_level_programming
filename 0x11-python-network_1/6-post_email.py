#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
Also only two packages are allowed
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    req = requests.post(url, value)
    print(req.text)
