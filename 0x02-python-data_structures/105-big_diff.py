#!/usr/bin/python3
def big_diff(my_list=[]):
    if len(my_list) == 0:
        return None
    min, max = my_list[0], my_list[0]
    for n in my_list:
        if n < min:
            min = n
        if n > max:
            max = n
    return max - min
