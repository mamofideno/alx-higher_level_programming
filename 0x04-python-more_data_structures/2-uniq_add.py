#!/usr/bin/python3
def uniq_add(my_list=[]):
    my=[]
    sum=0
    for i in my_list:
        if i not in my:
            sum+=i
            my.append(i)
    return sum
