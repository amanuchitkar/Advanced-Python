class Employee:
    no_of_leaves = 6

    def __init__(self, nameis, salaryis, roleis):
        self.name = nameis
        self.salary = salaryis
        self.role = roleis

    def print_a(self):
        return f"The name is {self.name}. Salary is {self.salary} and the role is {self.role}"

    @classmethod
    def change_leaves(cls, newLeave):
        cls.no_of_leaves = newLeave


nayan = Employee("Nayan kolhatkar", 25555, "Government officer")
# print(nayan.print_a())
# print(nayan.no_of_leaves)
# Employee.no_of_leaves = 34
nayan.change_leaves(34)
print(nayan.no_of_leaves)
