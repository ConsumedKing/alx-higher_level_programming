#!/usr/bin/python3
"""
Class Rectangle Real Definition
"""


class Rectangle:
    """ Rectangle Class """
    def __init__(self, width=0, height=0):
        """ init """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width getter """
        return self.__width

    @property
    def height(self):
        """ height getter """
        return self.__height

    @width.setter
    def width(self, value):
        """ width setter """
        if value < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        self.__width = value

    @height.setter
    def height(self, value):
        """ height setter """
        if value < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        self.__height = value
