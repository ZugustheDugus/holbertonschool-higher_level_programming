#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    srt = dict(sorted(a_dictionary.items()))
    for i in srt:
        print("{}: {}".format(i, srt[i]))
