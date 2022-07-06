#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    janeDel = []
    for i, j in a_dictionary.items():
        if j == value:
            janeDel.append(i)
    for i in janeDel:
        a_dictionary.pop(i)
    return a_dictionary
