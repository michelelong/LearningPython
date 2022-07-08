#!/usr/local/bin/python3

class Person:
    # Static member variables are available to the class itself
    howMany = 0

    # Initialize objects of Person class
    # self is the calling instance
    def __init__(self, name, age):
        # Instance variables are available to specific instances of the class
        self.name = name
        self.age = age
        Person.howMany += 1

    # Getter and setter methods allow for input validation and limit external access
    def setName(self, newName):
        if type(newName) is str:
            self.name = newName

    def setAge(self, newAge):
        if type(newAge) is int and newAge > 0 or newAge < 130:
            self.age = newAge

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    # Class method that takes another instance as the second parameter
    def shakeHands(self, other):
        print("%s shakes hands with %s." % (self.name, other.name))

    # Static method does not need self parameter
    # Accessible by the class without an instance
    @staticmethod
    def greet():
        print("Hello.")

    # When print is called on an object, it looks for a __repr__() method,
    # Override the default object printing
    def __repr__(self):
        return ("My name is %s and I am %s years old." % (self.name, self.age))


# Create class instances, runs the init method
michele = Person("Michele", 99)

# Printing an object calls __repr__ method
print(michele)

# Call setter method to change age
michele.setAge(15)
print(michele)

print()

jane = Person("Jane", 27)
print(jane)

# Call getter method for age
print("Jane is %i years old."% (jane.getAge()))

print()

# Accessing a static method does not require an instantiated object
Person.greet()

# michele will be the 'self' referred in the method
# jane is the other referred to in the method
michele.shakeHands(jane)

print()

# Static variables can be accessed without creating an instance
print("How many people are there? ", Person.howMany)

# Does not change the class variable Person.howMany
michele.howMany = 15
# It creates an instance variable with the same name
print("Michele's howMany:", michele.howMany)

print("There are still the same # of people: ", Person.howMany)

# Nested Classes
# Car is the outer class
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        self.engine = self.Engine() # Initialize inner class object

    def startEngine(self):
        self.Engine.start(self.brand) # Access the inner class method

    def __repr__(self):
        return "This car is a %i %s." % (self.year, self.brand)

    #Engine is the inner class
    class Engine:
        def start(brand):
            print("Vroom vroom goes the %s!" % (brand))

print()

myCar = Car("Toyota", 2009)
print(myCar)
myCar.startEngine()
