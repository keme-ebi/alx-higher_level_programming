#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tup_a, tup_b = len(tuple_a), len(tuple_b)

    if tup_a == 0:
        a1 = 0
        a2 = 0
    elif tup_a == 1:
        a1 = tuple_a[0]
        a2 = 0
    else:
        a1 = tuple_a[0]
        a2 = tuple_a[1]

    if tup_b == 0:
        b1 = 0
        b2 = 0
    elif tup_b == 1:
        b1 = tuple_b[0]
        b2 = 0
    else:
        b1 = tuple_b[0]
        b2 = tuple_b[1]

    new = (a1 + b1, a2 + b2)
    return new
