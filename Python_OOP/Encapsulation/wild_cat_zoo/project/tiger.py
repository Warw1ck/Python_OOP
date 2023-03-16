from pizza_maker.project import Animal


class Tiger(Animal):
    amount_of_money_to_be_cared_for = 45

    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, self.amount_of_money_to_be_cared_for)