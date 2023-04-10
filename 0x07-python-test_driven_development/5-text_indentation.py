#!/usr/bin/python3
"""5-text_indentation module that contains only 1 function"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters
       ``. ? and :
       Arg:
           text(str): text to be printed
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    space_ctrl = 0

    for i in text:
        if space_ctrl == 0:
            if i == ' ':
                continue
            else:
                space_ctrl = 1
        if space_ctrl == 1:
            if i == '.' or i == '?' or i == ':':
                print(i)
                print()
                space_ctrl = 0
            else:
                print(i, end="")
