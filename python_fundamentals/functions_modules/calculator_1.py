#!/usr/bin/env python3

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multi(a, b):
    return a * b

def division(a, b):
    return a / b



if __name__ == "__main__":
    a = 10
    b = 5
    print("suma: {}, resta: {}, multiplicación: {}, división: {}".format(suma(a, b), resta(a, b), multi(a, b), division(a, b)))
