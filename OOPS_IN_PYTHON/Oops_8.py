class Employee:
    noOfLeaves = 5
    var = 6

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def display(self):
        return f"The name is {self.name}. Salary is {self.salary} and job role is {self.role}"

    @classmethod
    def change_leaves(cls, noOfLeaves):
        cls.no_of_leaves = noOfLeaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)


class Player:
    no_of_games = 4
    var = 8

    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printD(self):
        return f"The player name is {self.name} and play game is {self.game}"


class cool_prog(Employee, Player):
    var = 10
    language = "C++"

    def print_language(self):
        print(self.language)


harry = Employee("Harry", 255, "Instructor")
print(harry.display())
nayan = Player("Nayan", ["cricet"])
aman = cool_prog("aman", 000000, "kuch ni")
aman.print_language()
print(aman.var)
print(nayan.var)
print(harry.var)

# print(nayan.printD())
