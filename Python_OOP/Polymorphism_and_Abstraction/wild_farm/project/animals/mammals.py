from project.animals.animal import Mammal
from project.food import Vegetable, Meat, Fruit


class Mouse(Mammal):
    EAT = [Vegetable, Fruit]
    GAIN_WEIGHT = 0.10
    FoodEaten = 0

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "Squeak"

    def feed(self, food):
        if type(food) not in self.EAT:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.FoodEaten += food.quantity
        self.weight += self.GAIN_WEIGHT * food.quantity


class Dog(Mammal):
    EAT = [Meat]
    GAIN_WEIGHT = 0.40
    FoodEaten = 0

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "Woof!"

    def feed(self, food):
        if type(food) not in self.EAT:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.FoodEaten += food.quantity
        self.weight += self.GAIN_WEIGHT * food.quantity


class Cat(Mammal):
    EAT = [Meat, Vegetable]
    GAIN_WEIGHT = 0.30
    FoodEaten = 0

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "Meow"

    def feed(self, food):
        if type(food) not in self.EAT:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.FoodEaten += food.quantity
        self.weight += self.GAIN_WEIGHT * food.quantity


class Tiger(Mammal):
    EAT = [Meat]
    GAIN_WEIGHT = 1.00
    FoodEaten = 0

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "ROAR!!!"

    def feed(self, food):
        if type(food) not in self.EAT:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.FoodEaten += food.quantity
        self.weight += self.GAIN_WEIGHT*food.quantity


