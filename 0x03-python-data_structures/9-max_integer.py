#!/usr/bin/python3
def max_integer(my_list=[]):
    lrgst = my_list[0]

    for li in my_list:
        if li > lrgst:
            lrgst = li

    return lrgst
