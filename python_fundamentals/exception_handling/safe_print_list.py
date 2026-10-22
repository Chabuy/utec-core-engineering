#!/usr/bin/env python3

def safe_print_list(my_list=[], x=0):
    quantity = 0
    for item in range(x):
        try:
            print("{:d}".format(my_list[item]), end="")
        except (TypeError, IndexError):
            continue
        quantity += 1
    print()
    return quantity
