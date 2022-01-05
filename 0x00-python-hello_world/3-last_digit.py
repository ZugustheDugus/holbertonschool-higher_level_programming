#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = number % 10
if number < 0:
    ld = ((number * -1) % 10) * -1
if ld > 5:
    print("Last digit of %d is %d and is greater than 5" % (number, ld))
if ld == 0:
    print("Last digit of %d is %d and is 0" % (number, ld))
if ld < 6 and ld != 0:
    print("Last digit of %d is %d and is less than 6 and not 0" % (number, ld))
