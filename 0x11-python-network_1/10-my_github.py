#!/usr/bin/python3
""" Uses GitHub API to display id """

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = 'https://api.github.com/user'

    response = requests.get(url, auth=(username, token))

    try:
        data = response.json()

        if isinstance(data, dict) and "id" in data:
            print(data["id"])
        else:
            print("None")
    except ValueError:
        print("Not a valid JSON")
