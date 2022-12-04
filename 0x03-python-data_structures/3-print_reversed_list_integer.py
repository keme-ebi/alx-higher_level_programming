#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        pass
    else:
        rev = reversed(my_list)
        for num in rev:
            print("{:d}".format(num))
