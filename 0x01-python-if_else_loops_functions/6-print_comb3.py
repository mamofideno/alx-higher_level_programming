#!/usr/bin/python3
for ii in range(0, 9):
    for i in range(ii + 1 , 10):
        if i == 8 and ii == 9:
            print("{}{}".format(ii,i))
        print("{}{}, ".format(ii, i), end="")
