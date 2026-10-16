#!/usr/bin/env python3

def print_list_integer(my_list=[]):
    for i in my_list:
        print("{:d}".format(i))

# if __name__ == "__main__":
#     my_list = [1,2,3]
#     result = print_list_integer(my_list)
#     print("\n".join("{:d}".format(v) for v in result))
