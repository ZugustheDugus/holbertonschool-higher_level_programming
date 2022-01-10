#!/usr/bin/python3
def common_elements(set_1, set_2):
    c_list = []
    c_set = set(c_list)
    for i in set_1:
        if i in set_1 and i in set_2:
            c_set.add(i)
    return c_set
