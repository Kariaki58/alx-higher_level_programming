#!/usr/bin/python3
"""
response header value #0
"""
from urllib.request import urlopen
import sys


if __name__ == "__main__":
    with urlopen(sys.argv[1]) as response:
        """with with statment"""
        headers = response.headers
        print(headers.get('X-Request-Id'))
