class Animal:
    def eat(self):
        print("om nom nom")
    def sleep(self):
        print("zzz")

class Prey(Animal):
    def flee(self):
        print("bye bye")

class Predator(Animal):
    def hunt(self):
        print("im going to eat you")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
rabbit.flee()

hawk = Hawk()
hawk.hunt()

fish = Fish()
fish.flee()
fish.hunt()

rabbit.eat()
rabbit.sleep()