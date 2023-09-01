#!/usr/bin/python3
"""Module to be used to help with that takes in a URL, sends a request to
the URL and displays the body of the response
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            body = response.read()
            print(body.decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
