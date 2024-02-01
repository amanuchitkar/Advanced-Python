class Employee:
    def __init__(self, a, b):
        self.fname = a
        self.lname = b

    def __repr__(self):
        return f"Anything('{self.fname}', '{self.lname}')"

    @property
    def email(self):
        if self.fname == None or self.lname is None:
            return "Email is not set yet"
        return f"{self.fname}.{self.lname}@uchitkargroups.in.net"

    @email.setter
    def email(self, string):
        names = string.split("@")[0]
        bothname = names.split(".")
        self.fname = bothname[0]
        self.lname = bothname[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


pranav = Employee("pranav", "dhandara")
# print(type(pranav))
# print(id(pranav))
# print(dir(pranav))

import inspect
print(inspect.getmembers(pranav))
