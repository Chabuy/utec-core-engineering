#!/usr/bin/env python3
"""Módulo que define la clase Square."""


class BaseGeometry:
    """Representa una base geometrica."""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Representa un rectangulo."""

    def __init__(self, width, height):
        super().integer_validator("widght", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
