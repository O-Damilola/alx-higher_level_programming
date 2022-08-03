#!/usr/bin/python3
# 1-write_file.py
"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """Write a string to UTF-8 text file.
    Args:
        filename (str): The name of the file to write into.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as don:
        don.write(text)
    return len(text)
