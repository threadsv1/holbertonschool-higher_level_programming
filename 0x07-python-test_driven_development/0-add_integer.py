#!/usr/bin/python3
"""
Integers Addition Module
"""


def add_integer(a, b=98):
"""
 adds 2 integers
"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integr")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if (a + b) == float('inf') or (a + b) == -float('inf'):
        return b
    return int(a) + int(b)
