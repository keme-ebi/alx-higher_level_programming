#!/usr/bin/python3
"""module with one function that creates an object from a JSON file"""


import json


def load_from_json_file(filename):
    """creates an object from a JSON file
       Arg:
           filename: file to create object from
    """
    with open(filename, encoding='utf-8') as f:
        return json.load(f)
