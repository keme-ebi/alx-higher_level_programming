#!/usr/bin/python3
for i in range(9):
    for b in range(10):
        if i < b:
            if i != 8 or (i == 8 and b != 9):
                print("{:d}{:d}".format(i, b), end=", ")
            else:
                print("{:d}{:d}".format(i, b))
