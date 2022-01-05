#!/usr/bin/python3
def uppercase(str):
    new_string = ''
    for i in str:
        char = ord(i)
        if ord('a') <= char <= ord('z'):
            char -= 32
        new_string += chr(char)
    print('{}'.format(new_string))
