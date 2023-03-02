class Employee:
    def __init__(self, id, name, last_name, salary):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self):
        return f'{self.name} {self.last_name}'

    def raise_salary(self, money):
        self.salary += money
        return self.salary

    def get_annual_salary(self):
        return self.salary*12

employee = Employee(744423129, "John", "Smith", 1000)
print(employee.get_full_name())
print(employee.raise_salary(500))
print(employee.get_annual_salary())
