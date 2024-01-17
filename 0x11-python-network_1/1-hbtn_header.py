#!/usr/bin/python3
"""
response header value #0
"""
from urllib.request import urlopen
import sys


with urlopen(sys.argv[1]) as response:
    headers = response.headers
    print(headers.get('X-Request-Id'))
