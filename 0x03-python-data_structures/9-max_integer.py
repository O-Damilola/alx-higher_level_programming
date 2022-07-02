#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    maxi = 0
    for j in my_list:
        if maxi - j <= 0:
            maxi = j
    return (maxi)
