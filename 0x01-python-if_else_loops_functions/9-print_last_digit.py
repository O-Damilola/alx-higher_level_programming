#!/usr/bin/python3
def print_last_digit(number):
    str1 = str(number)
    list1 = list(str1)
    last_digit = list1[-1]
    return (last_digit)

print(print_last_digit(10246))
