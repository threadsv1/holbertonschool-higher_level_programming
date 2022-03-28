#!/usr/bin/python3
"""
Contains function that returns int lists of pascal triangle of any given size
"""


def pascal_triangle(i):
    """
    print pascal triangle
    """
    if i <= 0:
        return []
    if i == 1:
        return [[1]]

    triangle = [[1]]
    for rows in range(i-1):
        triangle.append([a+b for a, b
                         in zip([0] + triangle[-1], triangle[-1] + [0])])
    return triangle
