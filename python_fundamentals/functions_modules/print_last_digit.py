#!/usr/bin/env python3

def print_last_digit(number):
    digits = []
    for value in (str(number)):
        if value != "-":
            digits.append(int(value))
    last_digit= digits[-1]
    print(last_digit, end="")
    return last_digit
