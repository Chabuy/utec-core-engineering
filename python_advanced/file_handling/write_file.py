#!/usr/bin/env python3
"""This is a docstring using triple single quotes."""


def write_file(filename="", text=""):
    """This is a docstring using triple single quotes."""
    with open(filename, "w", encoding="utf-8") as file:
        content = file.write(text)
    return len(content)
