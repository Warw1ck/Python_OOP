class Topping:
    def __init__(self, topping_type: str, weight: float):
        self.topping_type = topping_type
        self.weight = weight

    @property
    def topping_type(self):
        return self.topping_type_check

    @topping_type.setter
    def topping_type(self, topping_type):
        if not topping_type:
            raise ValueError("The topping type cannot be an empty string")
        else:
            self.topping_type_check = topping_type

    @property
    def weight(self):
        return self.weight_check

    @weight.setter
    def weight(self, weight):
        if weight < 1:
            raise ValueError("The weight cannot be less or equal to zero")
        else:
            self.weight_check = weight
