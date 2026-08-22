
# "Duck typing" = Another way to achieve polymorphism besides inheritance
#                 Object must have the minimum necessary attributes/mrthods
#                 "If it looks like a duck and quacks like a ducks, it must be a duck"



class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("woof")

class Cat(Animal):
    def speak(self):
        print("meow")

class Car:
    alive = False

    def speak(self):
        print("honk")

animals = [Dog(), Cat(), Car()]

for x in animals:
    x.speak()
    print(x.alive)