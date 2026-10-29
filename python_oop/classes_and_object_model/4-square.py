#!/usr/bin/env python3
"""Módulo que define la clase Square."""


class Square:
    """Representa un cuadrado."""
    def __init__(self, size=0):
        self.__size = size

    def get_area(self):
        self.area = self.size * self.size
        return self.area

    
    def get_size(self):
        """Devuelve valor lados."""
        return self.__size

    
    def set_size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
