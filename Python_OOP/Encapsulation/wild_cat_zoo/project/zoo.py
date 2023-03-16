class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if not self.__animal_capacity:
            return "Not enough space for animal"
        if price > self.__budget:
            return "Not enough budget"

        self.animals.append(animal)
        self.__animal_capacity -= 1
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if not self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        self.__workers_capacity -= 1
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        try:
            worker = next(filter(lambda p: p.name == worker_name, self.workers))
            self.workers.remove(worker)
            self.__workers_capacity += 1
            return f"{worker_name} fired successfully"

        except StopIteration:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries = sum([worker.salary for worker in self.workers])
        if salaries > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        tend = sum([animal.money_for_care for animal in self.animals])
        if tend > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= tend
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = list(filter(lambda p: f'{p.__class__.__name__}' == 'Lion', self.animals))
        tigers = list(filter(lambda p: f'{p.__class__.__name__}' == 'Tiger', self.animals))
        cheetah = list(filter(lambda p: f'{p.__class__.__name__}' == 'Cheetah', self.animals))

        the_print = [f"You have {len(self.animals)} animals", f'----- {len(lions)} Lions:']

        for el in lions:
            the_print.append(f'{el}')
        the_print.append(f'----- {len(tigers)} Tigers:')
        for el in tigers:
            the_print.append(f'{el}')
        the_print.append(f'----- {len(cheetah)} Cheetahs:')
        for el in cheetah:
            the_print.append(f'{el}')

        return '\n'.join(the_print)

    def workers_status(self):
        keepers = list(filter(lambda p: f'{p.__class__.__name__}' == 'Keeper', self.workers))
        caretakers = list(filter(lambda p: f'{p.__class__.__name__}' == 'Caretaker', self.workers))
        vets = list(filter(lambda p: f'{p.__class__.__name__}' == 'Vet', self.workers))

        the_print = [f"You have {len(self.workers)} workers", f'----- {len(keepers)} Keepers:']

        for el in keepers:
            the_print.append(f'{el}')
        the_print.append(f'----- {len(caretakers)} Caretakers:')
        for el in caretakers:
            the_print.append(f'{el}')
        the_print.append(f'----- {len(vets)} Vets:')
        for el in vets:
            the_print.append(f'{el}')

        return '\n'.join(the_print)


