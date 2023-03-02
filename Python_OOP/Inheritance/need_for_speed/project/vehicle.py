class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel: float, horse_power: int, fuel_consumption=DEFAULT_FUEL_CONSUMPTION):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = fuel_consumption

    def drive(self, kilometers):
        needed_fuel = kilometers*self.DEFAULT_FUEL_CONSUMPTION
        if needed_fuel <= self.fuel:
            self.fuel -= needed_fuel

