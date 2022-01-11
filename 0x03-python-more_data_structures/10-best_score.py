#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        high = 0
        for key, val in a_dictionary.items():
            if val > high:
                high, newkey = val, key
        return newkey
