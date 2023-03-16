from pizza_maker.project.dough import Dough
from pizza_maker.project.topping import Topping


class Pizza:
    def __init__(self, name: str, dough: Dough, max_number_of_toppings: int):
        self.name = name
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings = {}
        self.toppings_num = 0

    @property
    def name(self):
        return self.name_check

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("The name cannot be an empty string")
        else:
            self.name_check = name

    @property
    def dough(self):
        return self.dough_check

    @dough.setter
    def dough(self, dough):
        if not dough:
            raise ValueError("You should add dough to the pizza")
        else:
            self.dough_check = dough

    @property
    def max_number_of_toppings(self):
        return self.max_number_of_toppings_check

    @max_number_of_toppings.setter
    def max_number_of_toppings(self, max_number_of_toppings):
        if max_number_of_toppings < 1:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")
        else:
            self.max_number_of_toppings_check = max_number_of_toppings

    def add_topping(self, topping: Topping):
        if self.toppings_num == self.max_number_of_toppings:
            raise ValueError("Not enough space for another topping")

        if topping.topping_type not in self.toppings:
            self.toppings[topping.topping_type] = 0

        self.toppings[topping.topping_type] += topping.weight
        self.toppings_num += 1

    def calculate_total_weight(self):
        return sum([el for el in self.toppings.values()]) + self.dough.weight



