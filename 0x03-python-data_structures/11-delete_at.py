#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list)-1:
        return (my_list)
    for ele in my_list:
        if ele == idx:
            del my_list[idx]    
    return (my_list)
