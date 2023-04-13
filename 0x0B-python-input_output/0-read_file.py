#!/usr/bin/python3
"""module with one function that reads a text file"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout
       Arg:
            filename(file): file to be read
    """
    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end="")
