class Employee:
    noOfLeaves = 5

    def __init__(self, a, b, c):
        self.name = a
        self.salary = b
        self.role = c

    def display(self):
        return f"The name is {self.name}. Salary is {self.salary} and job role is {self.role}"

    @classmethod
    def get(cls, new):
        cls.noOfLeaves = new

    @classmethod
    def from_str(cls, string):
        # params = string.split("-")
        # return cls(params[0], params[1], params[2])
        # return cls(*string.split("/"))
        return cls(*string.split("-"))


nayan = Employee("Nayan", 499, "Government job")
print(nayan.display())
# pranav = Employee.from_str("Pranav-6666000-YT_Gamer")
# print(pranav.display())
arthav = Employee.from_str("Krish rodge/9000000/IIT-job")
print(arthav.display())
