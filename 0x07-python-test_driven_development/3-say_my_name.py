#!/usr/bin/python3
"""Module for 3-say_my_name.py which has only one function in it"""


def say_my_name(first_name, last_name=""):
    """prints ``My name is <first_name> <last_name>
       Args:
            first_name(str): first name of user
            last_name(str): last name of user
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
