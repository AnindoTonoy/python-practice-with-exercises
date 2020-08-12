# defining a class
class Employee:
    no_of_leaves = 8

    # Constructor
    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age

    # action method
    def print_details(self):
        return f'The name is: {self.name}\nSalary: {self.salary}\nAge is: {self.age}'

    # operator overriding
    def __add__(self, other):
        return self.salary + other.salary

    def __mod__(self, other):
        return self.salary % other.salary

    def __repr__(self):
        return f'{self.name}, {self.salary}, {self.age}'


anindo = Employee('Anindo Dey', 50000, 24)
harry = Employee('Harry Potter', 40000, 24)

print(anindo % harry)
print(anindo)