# defining a class
class Employee:
    no_of_leaves = 8

    # Constructor
    def __init__(self, obj_name, obj_salary, obj_age):
        self.name = obj_name
        self.salary = obj_salary
        self.age = obj_age

    # action method
    def print_details(self):
        return f'The name is: {self.name}\nSalary: {self.salary}\nAge is: {self.age}'

    # this class method can change class variables access by objects and instances
    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    # class methods as alternative constructor
    @classmethod
    def from_dash(cls, str):
        return cls(*str.split("-"))


# Creating objects of employee class
anindo = Employee('Anindo Dey', 50000, 25)
harry = Employee('Harry Potter', 45000, 24)


class Player:
    no_of_leaves = 10

    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printdetails(self):
        return f'The player name is: {self.name}\nGame: {self.game}'


# multiple inheritances
class CoolProgramer(Employee, Player):
    # no_of_leaves = 20
    language = ['python', 'C++', 'javaScript']

    def printlang(self):
        print('Languages:', self.language)


# ratul = Player("Ratul", ["Cricket"])
# det = ratul.printdetails()
# print(det)

ricky = CoolProgramer("Ricky", 57000, 27)
print(ricky.print_details())
ricky.printlang()
print(ricky.no_of_leaves)
