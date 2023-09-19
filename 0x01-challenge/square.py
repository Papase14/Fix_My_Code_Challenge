#!/usr/bin/python3

class Square:
    """
    Represents a square shape and provides methods to calculate its area and perimeter.
    
    Attributes:
        width (int): The width of the square.
        height (int): The height of the square.
    """
    
    def __init__(self, width=0, height=0):
        """
        Initializes a square object with the given width and height.
        
        Args:
            width (int): The width of the square. Default is 0.
            height (int): The height of the square. Default is 0.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculates and returns the area of the square.
        
        Returns:
            int: The area of the square.
        """
        return self.width * self.width

    def perimeter(self):
        """
        Calculates and returns the perimeter of the square.
        
        Returns:
            int: The perimeter of the square.
        """
        return 4 * self.width

    def __str__(self):
        """
        Returns a string representation of the square.
        
        Returns:
            str: The string representation of the square.
        """
        return f"Width: {self.width}, Height: {self.height}"

if __name__ == "__main__":
    s = Square(width=12, height=12)
    print(s)
    print("Area:", s.area())
    print("Perimeter:", s.perimeter())

