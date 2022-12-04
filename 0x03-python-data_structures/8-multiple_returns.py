#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    f_char = sentence[0]

    if length == 0:
        f_char = None

    return length, f_char
