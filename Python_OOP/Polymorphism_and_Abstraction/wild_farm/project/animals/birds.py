from project.animals.animal import Bird
from project.food import Meat, Vegetable, Fruit, Seed


class Owl(Bird):
    EAT = [Meat]
    GAIN_WEIGHT = 0.25
    FoodEaten = 0

    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    def feed(self, food):
        if type(food) not in self.EAT:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.FoodEaten += food.quantity
        self.weight += self.GAIN_WEIGHT * food.quantity


class Hen(Bird):
    GAIN_WEIGHT = 0.35
    FoodEaten = 0
    EAT = [Meat, Vegetable, Fruit, Seed]

    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    @staticmethod
    def make_sound():
        return "Cluck"

    def feed(self, food):
        if type(food) not in self.EAT:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.FoodEaten += food.quantity
        self.weight += self.GAIN_WEIGHT * food.quantity


