# defining a class
class Employee:
    # Constructor
    def __init__(self, obj_name, obj_salary, obj_age):
        self.name = obj_name
        self.salary = obj_salary
        self.age = obj_age

    # action method
    def print_details(self):
        return f'The name is: {self.name}\nSalary: {self.salary}\nAge is: {self.age}'


# Creating objects of employee class
anindo = Employee('Anindo Dey', 50000, 25)
harry = Employee('Harry Potter', 45000, 24)
carry = Employee('Carry Morgan', 46000, 26)

print(anindo.print_details(), end='\n\n')
print(carry.print_details(), end='\n\n')
print(harry.print_details(), end='\n\n')