# Instance & Class Variables
class Employee:
    no_of_leaves = 5


nayan = Employee()
mayur = Employee()

nayan.name = "Nayan"
nayan.salary = 300333
nayan.role = "Instructor"

mayur.name = "Mayur"
mayur.salary = 89000
mayur.role = "Engineer"

# print(mayur.role, nayan.salary)
print(mayur.__dict__)
mayur.no_of_leaves = 1
print(mayur.__dict__)

print(nayan.__dict__)
nayan.no_of_leaves = 50
print(nayan.__dict__)

print(Employee.__dict__)
Employee.no_of_leaves = 7
print(Employee.__dict__)
