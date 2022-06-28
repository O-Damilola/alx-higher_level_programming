#!/usr/bin/python3

for x in range(0, 100):
    if x <= 9:
        print("0%d" %(x), end=', ')
    else:
        print("%d" %(x), end=', ')
print('\n')
