#!/usr/bin/python3
def print_last_digit(number):
    last_digit = None
    if (number < 0):
        number *= -1
    last_digit = number % 10
    print("{}".format(last_digit), end="")
    return last_digit
