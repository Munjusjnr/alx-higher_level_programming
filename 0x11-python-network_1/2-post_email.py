#!/usr/bin/python3
"""Modules to be used for the POST request"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    """script that takes in a URL and an email, sends a POST request to the
    passed URL with the email as a parameter, and displays the body of the
    response (decoded in utf-8)
    """
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print(body.decode("utf-8"))
