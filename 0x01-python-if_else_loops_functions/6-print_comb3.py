#!/usr/bin/python3

arr = []
for i in range(0, 10):
    for j in range(0, 10):
        if j not in arr:
            print("%d%d" %(i,j), end=', ')
        arr.append(i)
