class Animal:

    def __init__(self):
        self.age=1

    def eat(self):
        print("eat")


class Mammal(Animal):

    def __init__(self):
        self.weight=1
        super().__init__()
    def walk(self):
        print("walk")

class Fish(Animal):
    def swim(self):
        print("swim")

class Bird(Animal):
    def fly(self):
        print("fly")
class Chicken(Bird):
    pass ## bmultilevel inheritance bad chicken cant fly

m=Mammal()
m.eat()
print(m.age)
print(m.weight)