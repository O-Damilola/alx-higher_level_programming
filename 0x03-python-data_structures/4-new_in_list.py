#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list2 = my_list[0 ::]
    if idx < 0 or idx > len(my_list2)-1:
        return my_list2
    else:
        my_list2[idx] = element
        return my_list2


my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)
