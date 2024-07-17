#!/usr/bin/python3
"""defines a Square class"""


class Square():
    """the Square Class"""
    width = 0

    def __init__(self, *args, **kwargs):
        """ Square init function"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area(self):
        """ Area of the square """
        return self.width * self.width

    def permiter(self):
        """ Permiter of the square"""
        return (self.width * 4)

    def __str__(self):
        """ Square str function"""
        return "{}/{}".format(self.width, self.width)


if __name__ == "__main__":

    s = Square(width=12)
    print(s)
    print(s.area())
    print(s.permiter())
