#!/usr/bin/python3
"""a module with one function that returns an object rep. by a JSON string"""


import json


def from_json_string(my_str):
    """returns an object(Python data structure) represented by JSON string"""
    f_json = json.loads(my_str)
    return f_json
