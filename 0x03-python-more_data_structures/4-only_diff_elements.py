#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    od_list = []
    od_set = set(od_list)
    for i in set_1:
        if i not in set_2:
            od_set.add(i)
    for j in set_2:
        if j not in set_1:
            od_set.add(j)
    return od_set
