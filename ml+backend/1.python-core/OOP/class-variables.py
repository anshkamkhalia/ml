class Human:

    brains = 1
    dimensions = 3
    num_humans = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Human.num_humans += 1

    
human1 = Human("Bob", 2)
human2 = Human("Bob", 2)
human3 = Human("Bob", 2)


print(human1.name)
print(human1.age)

print(Human.brains)
print(Human.dimensions)

print(Human.num_humans)
