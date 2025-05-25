from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):

    def __init__(self, length):
        self.length = length

    def area(self):
        return (self.length**2)

class Circle(Shape):
    
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (3.14159 * self.radius**2)

class Triangle(Shape):

    def __init__(self, length, height):
        self.length = length
        self.height = height

    def area(self):
        return (self.length * self.height / 2)

shapes = [Circle(4), Square(5), Triangle(6,7)]

for shape in shapes:
    print(f"{shape.area()}")