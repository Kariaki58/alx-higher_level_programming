#!/usr/bin/python3
number = "Holberton"
try:
    print(f'{int(number)} Battery street')
except ValueError as e:
    print(e)
