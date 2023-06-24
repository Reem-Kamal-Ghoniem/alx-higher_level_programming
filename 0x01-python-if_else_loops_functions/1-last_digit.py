#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = abs(number) % 10
if number < 0:
    num = num * (-1)
if num > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, num))
if num < 6 and num != 0:
    print("Last digit of {} is {} ".format(number, num), end="")
    print("and is less than 6 and not 0")
if num == 0:
    print("Last digit of {} is {} and is 0".format(number, num))
