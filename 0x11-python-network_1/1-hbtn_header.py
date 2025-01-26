#!/usr/bin/python3
""" Py script that takes in a URL, sends a request to it and displays the value of X-Request-Id """

from urllib import request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with request.urlopen(url) as response:
        headers = response.headers
        print(headers.get("X-Request-Id"))
