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

    @staticmethod
    def print_good(string):
        print("This is good " + string)


# Creating objects of employee class
anindo = Employee('Anindo Dey', 50000, 25)
harry = Employee('Harry Potter', 45000, 24)

# static method calling through instance
anindo.print_good('anindo')

# static method calling through class
Employee.print_good("Employee")
