#!/usr/bin/python3
for i in range(0, 9):
    for j in range(0, 9):
        if i != j and j != i:
            print("{}{}".format(i, j), end=", ")
