#!/usr/bin/env python3
"""Módulo que define la clase Square que hereda de Rectangle."""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Representa un cuadrado."""

    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
