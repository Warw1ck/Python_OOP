from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    AIR_CONDITIONER = 0.9

    def drive(self, distance):
        result = (self.fuel_consumption+Car.AIR_CONDITIONER)*distance
        if self.fuel_quantity >= result:
            self.fuel_quantity -= result

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AIR_CONDITIONER = 1.6

    def drive(self, distance):
        result = (self.fuel_consumption+Truck.AIR_CONDITIONER)*distance
        if self.fuel_quantity >= result:
            self.fuel_quantity -= result

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
