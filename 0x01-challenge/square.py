#!/usr/bin/python3
"""Defines a square module."""


class Square():
    """A square classs"""

    # width = 0
    # height = 0

    def __init__(self, width=0, height=0, *args, **kwargs):
        """Initialize a square"""
        self.width = width
        self.height = height

        # for key, value in kwargs.items():
        #    setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """Return the perimeter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Pretty print a square"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
