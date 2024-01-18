#!/usr/bin/python3
"""import modules"""
import requests
import sys


if __name__ == "__main__":
    usr = sys.argv[1]
    passwd = sys.argv[2]

    url = 'https://api.github.com/user'
    headers = {'Authorization': f'Bearer {passwd}'}
    try:
        response = requests.get(url, headers=headers)
        reponse_json = response.json()
        if 'id' in reponse_json:
            print(reponse_json['id'])
        else:
            print("None")
    except ValueError:
        print("None")
