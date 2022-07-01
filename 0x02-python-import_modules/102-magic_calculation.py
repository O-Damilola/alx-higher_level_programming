#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add as sum, sub as diff
    if a < b:
        c = sum(a, b)
        for i in range(4, 6):
            c = sum(c, i)
        return (c)
    else:
        return (diff(a, b))
