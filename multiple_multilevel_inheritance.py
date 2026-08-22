
# MULTIPLE INHERITANCE = inherit from more than one parent class
#                        C(A, B) #class c inherits from a and also b

# MULTILEVEL INHERITANCE = inherit from a parent which inherits from another parent
#                          C(B) <- B(A) <- A #



#multiple inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Prey(Animal): #prey and pred will inherit everything Animal class has
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")


class Rabbit(Prey): #rabbit, hawk and fish will inherit everything prey and pred class has
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bugs the rabbit")
hawk = Hawk("Tony the hawk")
fish = Fish("Nemo the fish")

rabbit.eat()


