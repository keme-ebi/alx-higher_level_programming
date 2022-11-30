#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(str(number)[-1])
string = "Last digit of"
if last_digit > 5:
    print(string,"{} is {} and is greater than 5".format(number, last_digit))
elif last_digit == 0:
    print(string,"{} is {} and is 0".format(number, last_digit))
elif last_digit < 6 and not 0:
    print(string,"{} is {} and is less than 6 and not 0".format(number, last_digit))
