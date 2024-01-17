#!/usr/bin/python3
"""Error code #0"""
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from urllib.parse import urlencode
import sys


if __name__ == "__main__"
    url = sys.argv[2]
    try:
        with urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as err:
        print(f'Error code: {err.code}')
