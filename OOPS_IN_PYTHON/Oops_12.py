# TuT #65
class A:
    classVar1 = "This is a class var1__1 in class A"

    def __init__(self):
        self.var1 = "This is var1 in class A instance Init"
        self.classVar1 = "This is a class var1 in instance A Init"
        self.special = "special From __Init__ 1 class A"


class B(A):
    classVar1 = "This is a class var2__2 in class A"

    def __init__(self):
        self.var1 = "This is var1 in class B instance Init"
        self.classVar1 = "This is a class var1 in instance B Init"
        super().__init__()


x = A()
y = B()
print(y.var1)
print(y.classVar1)
print(y.special)
