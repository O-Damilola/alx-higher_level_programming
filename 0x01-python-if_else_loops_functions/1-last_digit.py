#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(number)
numberstr = str(number)
numberarr = list(numberstr)
x = int(numberarr[-1])
if x == 0 and (number > 0 or number < 0):
    print("Last digit of {} is {} and is 0".format(number, x))
elif number > 0 and x != 0:
    if x > 5:
        print("Last digit of {} is {} and is greater than 5".format(number, x))
    else:
        print("Last digit of {} is {} and is less than 6 and not 0".format(number, x)) 
else:
    print("Last digit of %d is -%d and is less than 6 and not 0".format(number, x))
