#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = abs(number) % 10
print(f"Last digit of {number} is {num}", end="")
if num > 5:
    print("and is greater than 5")
if num < 6 and num != 0:
    print("and is less than 6 and not 0")
if num = 0:
    print("and is 0")
