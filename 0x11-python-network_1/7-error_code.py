#!/usr/bin/python3
""" sends request to a URL and displays the body """

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]

    response = requests.get(url)

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
