#!/usr/bin/python3
"""Defines a square module."""


class Square():
    """A square classs representing a square.

       Attr:
        - width: Width of the square.
        - height: Height of the square.
    """

    def __init__(self, width=0, height=0):
        """Initialize a square with a given width and height

           Args:
               @width: width of the square
               @heigh: heigth of the square
        """
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """ Area of the square.

            Returns: Area of the square
        """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """Caculates the permiter of the squre.

           Returns: The perimeter of the square
        """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Print a string representation of the square

           Return: A string reprsentation of the square.
        """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
