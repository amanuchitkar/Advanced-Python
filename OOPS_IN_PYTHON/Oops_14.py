class School:
    def __init__(self, a, b, c, d):
        self.name = a
        self.rollNo = b
        self.Class = c
        self.stendert = d

    def printS(self):
        return f"In school student name is {self.name} his/her roll no. {self.rollNo}" \
               f" and class is {self.Class} {self.stendert}"

    def __add__(self, other):
        return self.rollNo + other.rollNo

    def __repr__(self):
        return f"School('{self.name}', {self.rollNo}, {self.Class}, '{self.stendert}')"

    def __str__(self):
        return f"In school student name is {self.name} his/her roll no. {self.rollNo}" \
               f" and class is {self.Class} {self.stendert}"


stu1 = School("Aman", 56, 12, "A")
stu2 = School("Ashutosh soni", 45, 12, "A")
# print(stu1 + stu2)
print(repr(stu1))
print(str(stu1))
print(stu2)
