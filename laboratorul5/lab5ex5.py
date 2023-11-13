class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        pass

    def move(self):
        pass

class Mammal(Animal):
    def __init__(self, name, age, furColor):
        super().__init__(name, age)
        self.furColor = furColor

    def giveBirth(self):
        print(f"{self.name} is giving birth.")

    def eat(self):
        print(f"{self.name} is eating.")

    def move(self):
        print(f"{self.name} is moving.")

class Bird(Animal):
    def __init__(self, name, age, featherColor):
        super().__init__(name, age)
        self.featherColor = featherColor

    def layEggs(self):
        print(f"{self.name} is laying eggs.")

    def eat(self):
        print(f"{self.name} is eating.")

    def move(self):
        print(f"{self.name} is flying.")

class Fish(Animal):
    def __init__(self, name, age, scaleColor):
        super().__init__(name, age)
        self.scaleColor = scaleColor

    def layEggs(self):
        print(f"{self.name} is laying eggs.")

    def eat(self):
        print(f"{self.name} is eating.")

    def move(self):
        print(f"{self.name} is swimming.")

mammal = Mammal("Cat", 6, "Black")
bird = Bird("Sparrow", 4, "Brown")
fish = Fish("Shark", 2, "Silver")

mammal.eat()
mammal.giveBirth()

bird.eat()
bird.layEggs()

fish.eat()
fish.layEggs()

print(f"The {mammal.name} has {mammal.furColor} fur.")
print(f"The {bird.name} has {bird.featherColor} feathers.")
print(f"The {fish.name} has {fish.scaleColor} scales.")
