class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled


class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__
        self.radius = radius
        

class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__
        self.width = width
        

class Triangle(Shape):
    def __init__(self, color, filled, height, width):
        super().__init__
        self.width = width
        self.height = height
        