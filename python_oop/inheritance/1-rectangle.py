#!/usr/bin/env python3
"""Módulo que define la clase Rectangle que hereda de BaseGeometry."""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representa un rectangulo."""

    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
