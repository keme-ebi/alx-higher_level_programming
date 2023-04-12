#!/usr/bin/python3
"""0-lookup module which has only one function in it"""


def lookup(obj):
    """returns the list of available attributes and methods of an object"""
    return dir(obj)
