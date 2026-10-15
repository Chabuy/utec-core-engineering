#!/usr/bin/env python3

from calculator_1 import suma, resta, multi, division

if __name__ == "__main__":
    a = 10
    b = 5
    print("suma: {}, resta: {}, multiplicación: {}, división: {}".format(suma(a, b), resta(a, b), multi(a, b), division(a, b)))
