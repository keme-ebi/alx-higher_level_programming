#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    copy = ""
    for c in str:
        if i != n:
            copy += c
        i += 1
    return copy
