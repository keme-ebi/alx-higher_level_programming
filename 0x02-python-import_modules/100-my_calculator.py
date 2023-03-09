#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    n_args = len(argv) - 1
    if n_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    optr = argv[2]
    if optr != '+' and optr != '-' and optr != '*' and optr != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    from calculator_1 import add, sub, mul, div
    a = int(argv[1])
    b = int(argv[3])

    if optr == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif optr == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif optr == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("{} / {} = {}".format(a, b, div(a, b)))
