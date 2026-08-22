
# Polymorphism = Greek word that means to "have many forms or faces"
#                Poly = Many
#                Morphe = Form

#                Two ways to achieve polymorphism
#                1. Inheritance = An object could be treated of the same type as a parent class
#                2. "Duck typing" = Object must have necessary attributes/methods


#1.

from abc import ABC, abstractmethod

class Shape:

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * 3.14

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5


class Pizza(Circle): #inherits from circle class
    def __init__(self, topping, radius):
        self.topping = topping
        super().__init__(radius) #super func to get the radius from circle class

shapes = [
    Circle(4),
    Square(5),
    Triangle(6, 7),
    Pizza(  "Tomato", 15)
]

for x in shapes:
    print(f"{x.area()}cm^2")

