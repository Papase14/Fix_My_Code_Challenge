#!/usr/bin/python3

class Square:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        """ Area of the square """
        return self.width * self.width

    def perimeter(self):
        """ Perimeter of the square """
        return 4 * self.width

    def __str__(self):
        return f"Width: {self.width}, Height: {self.height}"

if __name__ == "__main__":
    s = Square(width=12, height=12)
    print(s)
    print("Area:", s.area())
    print("Perimeter:", s.perimeter())

