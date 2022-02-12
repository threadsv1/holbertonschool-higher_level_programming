#!/usr/bin/python3
""" square class"""


class Square:
    """ Creates square """

    def __init__(self, size=0):
        """ Initializes square """
        self.__size = size

    @property
    def size(self):
        """ Finds size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Validates size is an integer that is greater than zero """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """ Finds area of square """
        return self.__size ** 2

    def __eq__(self, other):
        """ Check if square is equal to other square """
        return self.size == other.size

    def __ne__(self, other):
        """ Check if square is not equal to other square """
        return self.size != other.size

    def __gt__(self, other):
        """ Check if square is greater than other square """
        return self.size > other.size

    def __lt__(self, other):
        """ Check if square is less than other square """
        return self.size < other.size

    def __ge__(self, other):
        """ Check if square is greater than or equal to other square """
        return self.size >= other.size

    def __le__(self, other):
        """ Check if square is less than or equal to other square """
        return self.size <= other.size
