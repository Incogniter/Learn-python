from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def printdetails(self):
        return 0


class Square(Shape):
    type = "square"
    sides = 4

    def __init__(self):
        self.sidecm = 10

    def printdetails(self):
        return f'area of square is {self.sidecm*self.sidecm}'


s1 = Square()
print(s1.printdetails())
