#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dic = a_dictionary
    for key, value in sorted(dic.items()):
        print(key,':',value)
