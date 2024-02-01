class Anything:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

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
        name = names.split(".")
        self.fname = name[0]
        self.lname = name[1]

        # self.fname = names.split(".")[0]
        # self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


etn1 = Anything("aman", "uchitkar")
print(etn1.email)
etn1.fname = "ayush"
print(etn1.email)
etn1.email = "mrudul.meshram@uchitkargroups.in.net"
print(etn1.email)
# print(etn1)
del etn1.email
print(etn1.email)
