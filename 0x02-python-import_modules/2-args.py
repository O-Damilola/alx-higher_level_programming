#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv as arr
    if len(arr)== 1:
        print("{} arguments.".format(len(arr)-1)) 
    elif len(arr)== 2:
        print("{} argument:".format(len(arr)-1))
    else:
        print("{} arguments.".format(len(arr)-1))
        for i in arr:
            if i != 0 and i != len(arr):
                print("{}: {}".format(i, arr[i]), end='\n')
            if i != 0 and i == len(arr):
                print("{}: {}".format(i, arr[i]))
            


arr([Hello, Welcome, To, The, Best, School])
