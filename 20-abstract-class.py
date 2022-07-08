#!/usr/local/bin/python3
from abc import abstractmethod, ABC

# An abstract class may contain both implemented and unimplemented methods
# Abstract classes can not be instantiated

# Inheriting abstract's ABC enforces implementation in subclasses
class Car(ABC):
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    # Annotate method definition
    @abstractmethod
    def start(self):
        pass # This will be implemented in subclasses

    # This method will be inherited as usual and does not need to be implemented in subclasses
    def stop(self):
        print("The car is stopping.")


class ElectricCar(Car):
    def __init__(self, brand, year):
        super().__init__(brand, year)

    # Implement the abstract method from the superclass
    def start(self):
        print("The electric car is starting.")


class GasCar(Car):
    def __init__(self, brand, year):
        super().__init__(brand, year)

    # Implement the abstract method from the superclass
    def start(self):
        print("The gas car is starting.")


eleCar = ElectricCar("Hyundai", 2020)
eleCar.start()
eleCar.stop()

print()

gasCar = GasCar("Ford", 2019)
gasCar.start()
gasCar.stop()
