class Animal:

    def __init__(self, name):
        self.name = name
        self.isAlive = True

    def eat(self):
        print(f"{self.name}: om nom nom")
    
    def sleep(self):
        print(f"{self.name}: zzzzz")

class Dog(Animal):
    
    def speak(self):
        print("woof")

class Mouse(Animal):

    def speak(self):
        print("squeak")

class Cat(Animal):

    def speak(self):
        print("meow")

dog = Dog("doggo")
mouse = Mouse("skibidi mouse")
cat = Cat("smurf cattt")

print(dog.name)
print(dog.isAlive)
dog.eat()
dog.sleep()
dog.speak()