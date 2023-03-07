#!/usr/bin/python3
def uppercase(str):
    for char in range(len(str)):
        if ord(str[char]) >= 97 and ord(str[char]) <= 122:
            num = 32
        else:
            num = 0
        print("{:c}".format(ord(str[char]) - num), end="")
    print()
