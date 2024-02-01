# tut 66 vid no-67
class A:
    # pass
    def printf(self):
        return "This is printf from class AA"


class B(A):

    def printf(self):
        return "This is printf from class BBB"
    pass


class C(A):
    # pass
    def printf(self):
        return "This is printf from class CCCC"


class D(B, C):
    def printf(self):
        return "This is printf from class DDDDD"

    pass


a = A()
b = B()
c = C()
d = D()
print(d.printf())
