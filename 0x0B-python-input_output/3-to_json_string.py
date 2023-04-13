#!/usr/bin/python3
"""module with one function that returns JSON rep. of an object"""


import json


def to_json_string(my_obj):
    """returns the JSON representation of an object(string)"""
    j_string = json.dumps(my_obj)
    return j_string
