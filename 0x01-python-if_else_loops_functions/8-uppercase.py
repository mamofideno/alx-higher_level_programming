#!/usr/bin/env python3
def uppercase(str):
    ass = 0
    for i in str:
        if ord(i) >= 97:
            ass = ord(i) - 32
        else:
            ass = ord(i)
        print("{}".format(chr(ass)), end="")
    print()
