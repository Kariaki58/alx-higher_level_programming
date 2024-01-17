#!/usr/bin/python3
"""
response header value #0
"""
from urllib.request import urlopen, Request
from urllib.parse import urlencode
import sys


if __name__ == "__main__":
    data = {'email': sys.argv[2]}
    data = urlencode(data).encode('utf-8')
    P_request = Request(sys.argv[1], data=data, method='POST')
    with urlopen(P_request) as response:
        print(f"Email: {response.read().decode('utf-8')}")
