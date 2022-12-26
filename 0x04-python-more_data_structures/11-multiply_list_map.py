#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new_list = my_list.copy()

    mult = list(map(lambda x: number * x, new_list))
    return mult
