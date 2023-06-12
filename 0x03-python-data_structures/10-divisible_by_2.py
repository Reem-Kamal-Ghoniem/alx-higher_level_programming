#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """is the element can be divided by 2"""
    divisible_list = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            divisible_list.append(True)
        else:
            divisible_list.append(False)

    return divisible_list
