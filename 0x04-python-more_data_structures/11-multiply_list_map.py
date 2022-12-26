#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new_list = list(map(lambda x: abs(number) * x, my_list.copy()))
    return new_list
