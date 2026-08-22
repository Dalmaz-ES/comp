
# INHERITANCE = allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               class Child(Parent) also known as sub and super classes

class Animal: #attributing from this although class dog,else is empty
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is asleep")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} is barking")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} is meowing")

class Mouse(Animal):
    def speak(self):
        print(f"{self.name} is squeaking")

dog = Dog("Buddy")
cat = Cat("Noche")
mouse = Mouse("Mickey")

print(dog.name, dog.is_alive)
dog.eat()
dog.sleep()
dog.speak()


