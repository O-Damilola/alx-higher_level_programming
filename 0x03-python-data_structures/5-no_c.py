#!/usr/bin/python3
def no_c(my_string):
    strList = []
    for ele in my_string:
        if ele == chr(99) or ele == chr(67):
            continue
        strList.append(ele)
    strdList = ''.join(strList)
    return strdList
