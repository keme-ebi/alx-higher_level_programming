#!/usr/bin/python3
"""module that creates a python list, and then save them to a file"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"

try:
    p_list = load_from_json_file(filename)
except Exception:
    p_list = []

p_list.extend(sys.argv[1:])
save_to_json_file(p_list, filename)
