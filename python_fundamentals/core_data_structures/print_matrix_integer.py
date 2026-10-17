#!/usr/bin/env python3

def print_matrix_integer(matrix=[[]]):
    if row > 0:   
        for row in matrix:
            for value in row:
                line = " ".join("{:d}".format(value) for value in row)
            print(line)
