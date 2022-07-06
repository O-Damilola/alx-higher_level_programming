#!/usr/bin/python3
def common_elements(set_1, set_2):
    jane = set_1 & set_2
    return(jane)

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Javascript", "Perl" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))
