#!/usr/bin/python3
def roman_to_int(roman_string):
    int_list = []
    int_sum = 0
    roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    test = type(roman_string) != str
    if type(roman_string) is str and roman_string:
        str_list = list(roman_string)
        for i in str_list:
            int_list.append(roman[i])
        j = 0
        while j < len(int_list)-1:
            if int_list[j] < int_list[j+1]:
                int_sum += -int_list[j]
            else:
                int_sum += int_list[j]
            j += 1
        int_sum += int_list[-1]       
        return (int(int_sum))
    return 0

roman_number = None
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = 'VII'
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
