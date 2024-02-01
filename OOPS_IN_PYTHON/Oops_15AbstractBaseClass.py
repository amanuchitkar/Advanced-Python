# tut 68
from abc import ABC, abstractmethod


class shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0


class Rectangle(shape):
    type = "Rectangle"
    sides = 4

    def __init__(self):
        self.length = 7
        self.breath = 7

    def printarea(self):
        return self.length * self.breath


rec = Rectangle()
print(rec.printarea())
