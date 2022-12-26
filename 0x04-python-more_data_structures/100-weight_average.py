#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    up = 0
    down = 0

    for num in my_list:
        up += num[0] * num[1]
        down += num[1]

    return up / down
