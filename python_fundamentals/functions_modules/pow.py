#!/usr/bin/env python3

def pow(a,b):
    result=1

    for _ in range(b):
        result *= a

    return result



def integer_power(a, b):
    if exponent >= 0:
        return pow(a, b)

    if base == 0:
        raise ZeroDivisionError("zero cannot have a negative exponent")

    return 1 / pow(a, -b)