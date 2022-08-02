#!/usr/bin/python3
def read_file(filename=""):
    """ function that reads a file """
    with open(filename, encoding="utf-8") as jon:
        """ Opens the file to be read """
        for line in jon:
            print(line, end="")
