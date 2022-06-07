#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    lis= []
    for i in my_list:
        lis.append((i % 2) == 0)
    return lis
