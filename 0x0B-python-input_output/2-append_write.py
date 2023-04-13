#!/usr/bin/python3
"""module with a function that appends a string to a text file"""


def append_write(filename="", text=""):
    """a function that writes a string to a text file (UTF-8)\
        and returns the number of characters written
       Args:
            filename(file): name of file
            text(str): text to be written in the file
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
