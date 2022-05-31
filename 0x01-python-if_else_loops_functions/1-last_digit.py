#!/usr/bin/python3
import random
number = random.rand
md=number % 10
if md > 5:
        print(f"Last digit of {number} is {md} and is greater than 5")
elif md == 0:
        print(f"Last digit of {number} is {md} and is 0")
else:
        print(f"Last digit of {number} is {md} and and is less than 6 and not 0") 
