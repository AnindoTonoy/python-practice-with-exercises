# defining a class
class Employee:
    no_of_employee = 500  # class variable, can't change thorough instance variables
    pass


# Creating objects of employee class
anindo = Employee()
harry = Employee()

# Creating instances variables(variables of objects)
anindo.name = 'Anindo Dey'
anindo.age = 25
anindo.salary = 50000

harry.name = 'Harry Potter'
harry.age = 24
harry.salary = 40000

print(anindo.name, harry.age)
print(anindo.no_of_employee)

print(harry.__dict__)   # .__dict__ - return a dictionary of contain variables
harry.no_of_employee = 25
print(harry.__dict__)

# changing a class variables value can not be changed through instance value
print(Employee.__dict__)
