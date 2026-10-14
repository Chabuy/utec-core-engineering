#!/usr/bin/env python3

def pow(a, b):
    if b >= 0:
        return pow(a, b)

    if base == 0:
        raise ZeroDivisionError("zero cannot have a negative exponent")

    return 1 / pow(a, -b)