class Employee:
    no_of_leaves = 6

    def __init__(self, nameis, salaryis, roleis):
        self.name = nameis
        self.salary = salaryis
        self.role = roleis

    def print_a(self):
        return f"The name is {self.name}. Salary is {self.salary} and the role is {self.role}"


nayan = Employee("Nayan kolhatkar", 25555, "Government officer")
mrudul = Employee("Mrudul Meshram", 255550000, "Engineer")
ashutosh = Employee("Ashutosh Soni", 70000000, "Engineer")
aman = Employee("Aman uchitkar", 100, "Chapal ki dukan")
# nayan.name = "Nayan"
# nayan.salary = 20009978387
# nayan.role = "Government officer"
print(nayan.print_a())
print(aman.print_a())
print(ashutosh.print_a())
print(mrudul.print_a())
# print(nayan.no_of_leaves)
