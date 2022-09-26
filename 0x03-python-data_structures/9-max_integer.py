#!/usr/bin/python3
# 9-max_integer.py

def max_integer(my_list=[]):
    """Find the biggest integer of a list."""
    if len(my_list) == 0:
        return (None)

    max_no = my_list[0]
    for n in range(len(my_list)):
        if my_list[n] > max_no:
            max_no = my_list[n]

    return (max_no)
