#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    rome_dict = {'I': 1, 'IV': 4, 'V': 5, 'VI': 6, 'X': 10, 'IX': 9, 'XI': 11, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'D': 500, 'CM': 900, 'M': 1000}
    result = 0
    if roman_string in rome_dict:
        result = rome_dict[roman_string]
        return result
    for i in roman_string:
        result += rome_dict[i]
    return result
