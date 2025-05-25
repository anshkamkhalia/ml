class Car:

    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print("vroooooooooooooom")

    def stop(self):
        print("screeech")

car1 = Car("Honda", 2024, "red", True)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

car1.drive()
car1.stop()