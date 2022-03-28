#!/usr/bin/python3
'''Write a text to a file
'''


def write_file(filename="", text=""):
    '''Write to a file using with
    '''
    with open(filename, 'r', encoding='utf8') as f:
        i = 0
        for line in f:
            i += 1
        return i
