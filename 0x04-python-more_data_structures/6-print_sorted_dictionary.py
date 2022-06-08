#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    al=sorted(a_dictionary)
    for i in al:
        print("{}:{}".format(i,a_dictionary[i]))
