#!/usr/bin/python3                                                                                                                                    
def element_at(my_list, idx):
    for ele in my_list:
        if idx < 0 or idx > len(my_list)-1:
            return None
        if ele == idx and idx > 0:
            return my_list[ele]
