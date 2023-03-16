class Dough:
    def __init__(self, flour_type: str, baking_technique: str, weight: float):
        self.flour_type = flour_type
        self.baking_technique = baking_technique
        self.weight = weight

    @property
    def flour_type(self):
        return self.flour_type_check

    @flour_type.setter
    def flour_type(self, flour_type):
        if not flour_type:
            raise ValueError("The flour type cannot be an empty string")
        else:
            self.flour_type_check = flour_type

    @property
    def baking_technique(self):
        return self.baking_technique_check

    @baking_technique.setter
    def baking_technique(self, baking_technique):
        if not baking_technique:
            raise ValueError("The baking technique cannot be an empty string")
        else:
            self.baking_technique_check = baking_technique

    @property
    def weight(self):
        return self.weight_check

    @weight.setter
    def weight(self, weight):
        if weight < 1:
            raise ValueError("The weight cannot be less or equal to zero")
        else:
            self.weight_check = weight

