class Employee:
    def __init__(self, x, y, z):
        self.name = x
        self.salary = y
        self.role = z

    def printR(self):
        return f"The name is {self.name} the salary is {self.salary} and the job role is {self.role}"

    @classmethod
    def printY(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printX(string):
        print("This is good" + string)


nayan = Employee("Nayan", 7000, "job")
latish = Employee.printY("Latish-60000-Engineer")
print(nayan.printR())
print(latish.printR())
latish.printX("hello")
