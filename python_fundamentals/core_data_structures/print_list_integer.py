#!/usr/bin/env python3

def print_list_integer(my_list=[]):
    for i in range(5):
        my_list.append(i)
    return my_list


if __name__ == "__main__":
    result = print_list_integer()
    print("\n".join("{}".format(v) for v in result))