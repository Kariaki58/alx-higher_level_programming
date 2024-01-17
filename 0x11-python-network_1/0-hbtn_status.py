#!/usr/bin/python3
"""
what's my status? #0
"""
from urllib.request import urlopen


with urlopen('https://alx-intranet.hbtn.io/status') as response:
    content = response.read()
    decode_content = content.decode('utf-8')

    print('Body response:')
    print(f'\t- type: {type(content)}')
    print(f'\t- content: {content}')
    print(f'\t- utf8 content: {decode_content}')