#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_sum = [] 
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    while len(list_a) < 2:
        list_a.append(0)
    while len(list_b) < 2:
        list_b.append(0)
    y = list_a[0] + list_b[0]
    z = list_a[1] + list_b[1]
    list_sum.append(y)
    list_sum.append(z)
    tuple_sum = tuple(list_sum)
    return (tuple_sum)
