#!/usr/bin/python3
"""script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
Also only two packages are to be imported
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    data = {"q": q}

    response = requests.post(url, data)

    try:
        j_resp = response.json()
        if j_resp:
            print("[{}] {}".format(j_resp.get("id"), j_resp.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
