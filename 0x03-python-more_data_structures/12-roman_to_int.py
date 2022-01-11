#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    rome_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    dec, num = 0, 0

    for i in range(len(roman_string) - 1, -1, -1):
        if rome_dict[roman_string[i]]:
            num += rome_dict[roman_string[i]]
        else:
            num -= rome_dict[roman_string[i]]
        dec = rome_dict[roman_string[i]]
    return num
