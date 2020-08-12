from abc import ABC, abstractmethod


# this is abstract base class
class Shape(ABC):

    @abstractmethod
    def print_area(self):
        return 0


class Rectangle(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def print_area(self):
        return self.length * self.breadth


rec1 = Rectangle(2, 4)
print("Area:", rec1.print_area())