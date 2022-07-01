#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add as sum, sub as diff, mul as dub, div as rep
    a = 10
    b = 5
    print("{:d} + {:d} = {:d}".format(a, b, sum(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, diff(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, dub(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, rep(a, b)))
