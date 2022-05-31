#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        md = (-1 * number) % 10
    else:
        md = number % 10
    print("{}".format(md), end="")
    return md
