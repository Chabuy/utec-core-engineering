#!/usr/bin/env python3
"""This is a docstring using triple single quotes."""

def read_file(filename = ""):
    """This is a docstring using triple single quotes."""
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    print(content, end="")
