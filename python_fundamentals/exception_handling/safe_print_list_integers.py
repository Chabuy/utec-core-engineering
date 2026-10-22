#!/usr/bin/env python3

def safe_print_list_integers(my_list=[], x=0):
    quantity = 0
    for item in range(x):
        try:
            if type(my_list[item]) == int:
                print("{:d}".format(my_list[item]), end="")
                quantity += 1
        except (TypeError):
            continue
        except (IndexError):
            raise
            
    print()
    return quantity
