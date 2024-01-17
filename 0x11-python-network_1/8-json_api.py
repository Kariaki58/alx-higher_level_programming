#!/usr/bin/python3
"""search api"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]
    args = {'q': q}
    try:
        response = requests.post('http://0.0.0.0:5000/search_user', data=args)
        json_data = response.json()

        if not json_data:
            print("No result")
        else:
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
    except ValueError:
        print("Not a valid JSON")
