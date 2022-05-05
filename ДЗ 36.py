import random
import numbers

class Rectangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"rectangle: {self.a}*{self.b}"

    @staticmethod
    def area(rectangle):
        return rectangle.a * rectangle.b

    def __gt__(self, other):
        if isinstance(other, Rectangle):
            return self.area(self) > self.area(other)
        return f"different types"

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return not self > other
        return f"different types"

    def __add__(self, other):
        if isinstance(other, Rectangle):
            s = Rectangle.area(self) + Rectangle.area(other)
            side1 = random.randint(self.a, self.a + other.a)
            side2 = s / side1
            return Rectangle(side1, side2)
        return f"different types"

    def __mul__(self, n):
        if isinstance(n, numbers.Real):
            s = self.area(self) * n
            side1 = random.randint(self.a, self.a + n)
            side2 = s / side1
            return Rectangle(side1, side2)
        return f"different types"


rec1 = Rectangle(1, 4)
rec2 = Rectangle(3, 5)
rec3 = rec1 + rec2
#print(rec1)
#print(rec2)
#print(rec3)
#print(Rectangle.area(rec1))
#print(Rectangle.area(rec2))
#print(Rectangle.area(rec3))
#print(rec3 * 4)
#print(Rectangle.area(rec3 * 4))






