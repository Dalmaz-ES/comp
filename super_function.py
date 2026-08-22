
# super() = function used in a child lass to call methods from a parent class (superclass)
#           allows you to extend the functionality of the inherited methods


class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def describe(self):
        print(f"It is {self.color} and {"filled" if self.filled else "not filled"}")

class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius

    def describe(self):
        print(f"Its a circle with an area of {3.14 * self.radius ** 2}cm^2")
        super().describe() #parent function

class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width

    def describe(self):
        print(f"Its a square with an area of {self.width * self.width}cm^2")
        super().describe()

class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"Its a triangle with an area of {self.width * self.height / 2}cm^2")
        super().describe()

#ALL SHARE COLOR AND FILLED ATTRIBUTES
#so color and filled will be on a parent class


circle = Circle(color="red", filled=True, radius=5) # in this way no need write in order
square = Square("blue", True, 6)
triangle = Triangle("green", True, 7, 8 )


#print(square.filled)
#print(square.color)
#print(f"{square.width}cm")

triangle.describe()



