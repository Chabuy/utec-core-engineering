#!/usr/bin/env python3
"""Módulo que define la clase Square."""


class Square:
    """Representa un cuadrado."""
    def __init__(self, size=0):
        self.size = size

    def area(self):
        return self.__size ** 2

    def my_print(self):
        symbol = "#"
        width = self.size
        height = self.size
        offset = 2
        rows = [" " * offset + symbol * width for _ in range(height)]
        result = "\n".join(rows)
        print (result)

    @property
    def size(self):
        """Devuelve valor lados."""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
