#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_digit = number % 10
begin = "Last digit of"

if l_digit > 5:
    print("{} {} is {} and is greater than 5".format(begin, number, l_digit))
elif l_digit == 0:
    print("{} {} is {} and is 0".format(begin, number, l_digit))
elif l_digit < 6 and not 0:
    print("{} {} is {} and is less than 6 and not 0".format(begin, number, l_digit))
