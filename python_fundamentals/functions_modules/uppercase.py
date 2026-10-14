#!/usr/bin/env python3

def uppercase(str):
    for value in (str):
        ascii_code = ord(value)
        if 97 <= ascii_code <= 122:
            value = chr(ascii_code - 32)
        print("{}".format(value), end="")
    print()
