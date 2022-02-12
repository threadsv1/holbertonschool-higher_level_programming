#!/usr/bin/python3
"""square class
"""


class Square:
    """ Square class"""

    def __init__(self, size=0):
        """ initializes the square """
        self.__size = size

    def area(self):
        """ Set square area """
        return self.__size ** 2

    @property
    def size(self):
        """ Getter of size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter of size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    def my_print(self):
        """ Print a square from the size using ## """
        if self.__size == 0:
            print()
        else:
            for i in range(1, self.__size + 1):
                for j in range(1, self.__size + 1):
                    print("#", end="")
                print()
