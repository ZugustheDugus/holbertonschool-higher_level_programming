#!/usr/bin/python3
def comb(L):

    for i in range(0, 9):
        for j in range(0, 9):
                if i != j:
                    print(L[i], L[j])
