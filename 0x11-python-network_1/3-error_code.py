#!/usr/bin/python3
""" sends request to URL and displays body of the response decoded """

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = Request(url)

    try:
        with urlopen(req)as response:
            body = response.read()
            print(body.decode('utf-8'))
    except HTTPError as e:
        print('Error code:', e.code)
    except URLError as e:
        print('Reason:', e.reason)
