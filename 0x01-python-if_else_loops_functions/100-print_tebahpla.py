#!/usr/bin/python3
check = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - check)), end="")
    check = 32 if check == 0 else 0
