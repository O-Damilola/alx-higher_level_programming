#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add as sum, sub as diff, mul as dup, div as res
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, sum(a, b)))
    print("{} - {} = {}".format(a, b, diff(a, b)))
    print("{} * {} = {}".format(a, b, dup(a, b)))
    print("{} / {} = {}".format(a, b, res(a, b))) 
    
