#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """a function that divides element by element 2 lists"""
    newlist = []
    for i in range list_length
        try:
            out = my_list_1[i] / my_list_2[i]
        except (IndexError):
            print("out of range")
            out = 0
        except (ZeroDivisionError):
            print("division by 0")
            out = 0
        except (TypeError):
            print("wrong type")
            out = 0
        finally:
            newlist.append(out)
    return (newlist)
