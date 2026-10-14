#!/usr/bin/env python3


def print_last_digit(number):
    digits = []
    for value in (str(number)):
        if value != "-":
            digits.append(int(value))
    return abs(digits[-1])
    