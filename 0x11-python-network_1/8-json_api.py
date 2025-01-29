#!/usr/bin/python3
""" takes in a letter and sends a POST request """

import requests
import sys

if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"

    q = sys.argv[1] if len(sys.argv) > 1 else ""

    response = requests.post(url, data={"q": q})

    try:
        data = response.json()

        if data:
            print(f"[{data.get('id')}] {data.get('name')}")
        else:
            print("No result")

    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
