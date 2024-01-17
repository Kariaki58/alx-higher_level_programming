#!/usr/bin/python3
"""POST an email"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    email_dict = {'email': email}
    response = requests.post(url, data=email_dict)
    print(response.text)
