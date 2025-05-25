class Engine:
    def __init__(self, hp):
        self.hp = hp

class Wheel:
    def __init__(self, size):
        self.size = size

class Car:
    def __init__(self, make, model, hp, tire_size):
        self.make = make
        self.model = model
        self.engine = Engine(hp)
        self.tire_size = [Wheel(tire_size) for wheel in range(4)]

    def display(self):
        print(f"{self.make} {self.model} has {self.engine.hp} horsepower and a tire size of {self.tire_size[0].size} inches")

car = Car("Bughatti", "Veyron", 500, 20)
car.display()