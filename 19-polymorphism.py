#!/usr/local/bin/python3

# Duck typing polymorphism
class Duck:
    def talk(self):
        print("Quack!")


class Human:
    def talk(self):
        print("Hello!")


# Method result differs depending on type of object passed
def callTalk(obj):
    obj.talk()


daffy = Duck()
callTalk(daffy)

fred = Human()
callTalk(fred)

print("-----")
print()

class Car:
    def __init__(self, engine):
        self.engine = engine

    # Dependency Injection Polymorphism
    # Engine can be initialized with different engine classes
    def startEngine(self):
        self.engine.start()

class ElectricEngine:
    def start(self):
        print("It hums quietly.")

class GasEngine:
    def start(self):
        print("It rumbles loudly.")

# Create two types of engine objects
eleEng = ElectricEngine()
gasEng = GasEngine()

# Create two cars with engine objects
car1 = Car(eleEng)
car2 = Car(gasEng)

# Different types of engines start differently
car1.startEngine()
car2.startEngine()

print("-----")
print()

# Overloading Polymorphism
# The plus operator is overloaded to do different things depending on use

# Add integers
print(2 + 2)

# Concatentate strings
print("Hello" + " " + "World")

# Concatentate lists
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst3 = lst1 + lst2
print(lst3)

print("-----")
print()

class Employee:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hey, boss.")


class CEO(Employee):
    def __init__(self, name):
        # Inherit name from Employee
        super().__init__(name)

    def greet(self):
        print("Back to work, peon.")


# Runtime polymorphism
# Varible changes type based on object assigned to it
ceoEmily = CEO("Emily")
emp = Employee("Steve")

emp.greet()
ceoEmily.greet()
