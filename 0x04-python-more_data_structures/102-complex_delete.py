#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    janeDel = a_dictionary.copy()
    for k, v in janeDel.items():
        if value in v:
            del a_dictionary[k]
    return a_dictionary

