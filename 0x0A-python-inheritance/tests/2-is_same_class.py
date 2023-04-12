#!/usr/bin/python3
"""2-is_same_class module which has only one function in it"""


def is_same_class(obj, a_class):
    """this function returns True if the object is exactly an instance of the
           specified class; otherwise False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
