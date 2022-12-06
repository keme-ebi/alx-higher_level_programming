#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    lrgst = my_list[0]

    for li in my_list:
        if li > lrgst:
            lrgst = li

    return lrgst
