#!/usr/bin/env python3

def safe_print_list(my_list=[], x=0):
    new_list = []
    for item in range(x):
        try:
           new_list.append(my_list[item]) 
        except (TypeError, IndexError):
            continue
    print(f"{new_list}\nnb_print:{x}")
