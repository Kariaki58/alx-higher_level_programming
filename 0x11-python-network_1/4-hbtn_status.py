#!/usr/bin/python3
"""what's my status"""
import requests


if __name__ == "__main__":
    fetchapi = requests.get('https://alx-intranet.hbtn.io/status')
    content = fetchapi.content
    content = content.decode('utf-8')
    print('Body response:')
    print(f'\t- type: {type(content)}')
    print(f"\t- content: {content}")
