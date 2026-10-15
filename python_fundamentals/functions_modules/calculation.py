#!/usr/bin/env python3

from calculator_1 import suma, resta, multi, division

if __name__ == "__main__":
    a = 10
    b = 5
    print(f"{a} + {b} = {suma(a, b)} \n{a} - {b} = {resta(a, b)} \n{a} * {b} = {multi(a, b)} \n{a} / {b} = {division(a, b)}")