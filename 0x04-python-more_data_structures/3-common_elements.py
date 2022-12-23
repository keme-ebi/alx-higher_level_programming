#!/usr/bin/python3
def common_elements(set_1, set_2):
    first = set(set_1)
    second = set(set_2)

    if len(first.intersection(second)) > 1:
        return (first.intersection(second))
