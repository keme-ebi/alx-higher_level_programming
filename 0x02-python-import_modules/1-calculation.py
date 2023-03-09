#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5
    addi = add(a, b)
    subt = sub(a, b)
    mult = mul(a, b)
    divi = div(a, b)

    print("{} + {} = {}".format(a, b, addi))
    print("{} - {} = {}".format(a, b, subt))
    print("{} * {} = {}".format(a, b, mult))
    print("{} / {} = {}".format(a, b, divi))
