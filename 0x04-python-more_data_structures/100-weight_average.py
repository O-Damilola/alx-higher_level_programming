#!/usr/bin/python3
def weight_average(my_list=[]):
    sum = 0
    product = 0
    for k in my_list:
        product += k[0] * k[1]
        sum += k[1]
    print(sum)
    print(product)
    average = product / sum
    return average
