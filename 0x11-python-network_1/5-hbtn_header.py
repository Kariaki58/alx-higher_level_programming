#!/usr/bin/python3
"""response header value #1"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    for key, value in response.headers.items():
        if key == "X-Request-Id":
            print(value)
