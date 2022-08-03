#!/usr/bin/python3
# 2-append-write.py
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF-8 text file.
    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to a file.
    Returns:
        The number of characters appended.
    """
    with open(filename, mode="a", encoding="utf-8") as don:
        don.write(text)
    return len(text)
