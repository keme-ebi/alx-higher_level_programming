#!/usr/bin/python3
def weight_average(my_list=[]):
    numerator, denominator = 0, 0
    if not my_list:
        return 0
    else:
        for num in my_list:
            numerator += num[0] * num[1]
            denominator += num[1]
        return numerator / denominator
