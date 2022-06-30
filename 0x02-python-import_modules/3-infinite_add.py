#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv as arr
    arrlenght = len(arr)
    sum = 0
    for i in range(1, arrlenght):
        sum += int(arr[i])
    print("{:d}".format(sum))
