#!/usr/bin/python3
"""defines a Square class"""


class Square():
    """the Square Class"""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Square init function"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """ Permiter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Square str function"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
