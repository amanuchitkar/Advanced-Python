class Student:
    def __init__(self, a, b, c):
        self.name = a
        self.Class = b
        self.roll = c

    def display(self):
        return f"The student name is {self.name}. His class is {self.Class} and roll No.{self.roll}"

    @classmethod
    def from_str(cls, line):
        return cls(*line.split("-"))


class subStudent(Student):
    def __init__(self, a, b, c, d):
        self.name = a
        self.Class = b
        self.roll = c
        self.lang = d

    def print_prog(self):
        return f"The student name is {self.name}. His class is {self.Class} and roll No.{self.roll}. He now the " \
               f"languages are {self.lang} "


# nayan = Student("Nayan", "12th", 48)
# nayan = Student.from_str("Nayan Kolhatkar-12th-48")
# print(nayan.display())

anish = subStudent("Anish Mankani", "100th", 143, ['python'])
# mrudul = subStudent("Mrudul meshram", "12th", 51, "c++, python")
mrudul = subStudent("Mrudul meshram", "12th", 51, ['python', 'c++'])
print(anish.print_prog())
print(mrudul.print_prog())
