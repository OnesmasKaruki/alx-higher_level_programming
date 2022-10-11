#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    len_elem = 0
    try:
        for i in range(x):
            print("{:d}".format(my_list[i], end=''))
            len_elem += 1
    except (ValueError, TypeError):
        pass
    print()
    return len_elem
