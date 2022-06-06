#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    lis=[]
    for i in my_list:
        if i%2 == 0:
            lis.append(i)
    return lis
