#!/usr/bin/python3
don = 122
while don >= 97:
    if don % 2 == 0:
        print("{}".format(chr(don)), end="")
    else:
        print("{}".format(chr(don-32)), end="")
    don -= 1
