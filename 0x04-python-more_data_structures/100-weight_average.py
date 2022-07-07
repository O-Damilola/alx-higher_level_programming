#!/usr/bin/python3
def weight_average(my_list=[]):
    sum = 0
    product = 0
    if len(my_list) == 0:
        return 0
    for k in my_list:
        product += k[0] * k[1]
        sum += k[1]
    average = product/sum
    return average
