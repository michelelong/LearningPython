#!/usr/local/bin/python3
from abc import abstractmethod, ABC

# An interface is different from abstract because ALL methods must be abstract
class Car(ABC):
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class ElectricCar(Car):
    def __init__(self, brand, year):
        super().__init__(brand, year)

    def start(self):
        print("The electric car quietly starts.")

    def stop(self):
        print("The electric car quietly stops.")


class GasCar(Car):
    def __init__(self, brand, year):
        super().__init__(brand, year)

    def start(self):
        print("The gas car loudly starts.")

    def stop(self):
        print("The gas car sputters to a stop.")


eleCar = ElectricCar("Hyundai", 2020)
eleCar.start()
eleCar.stop()

print()

garCar = GasCar("Ford", 2019)
garCar.start()
garCar.stop()
