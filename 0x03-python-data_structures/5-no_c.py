#!/usr/bin/python3
def no_c(my_string):
    N = ""
    for i in my_string:
        if not (i == 'c' or i == 'C'):
            N += i
            return N
