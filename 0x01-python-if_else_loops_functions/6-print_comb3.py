#!/usr/bin/python3
for ii in range(0, 9):
    for i in range(ii + 1 , 10):
        if ii == 8 and i == 9:
            print("{}{}".format(ii,i))
        else:
            print("{}{}, ".format(ii, i), end="")
