class Person:

    def __init__(self, name, age, salary, profession):
        self.name = name
        self.age = age
        self. salary = salary
        self.profession = profession
    workinghours = 8

    def printdetails(self):
        return f'Name is {self.name}, Age is {self.age}, Salary is {self.salary}, Profession is {self.profession},' \
               f' Working {self.workinghours} hours a day'

    # to change the fixed values in the class
    @classmethod
    def changeworkinghours(cls, newworkinghour):
        cls.workinghours = newworkinghour

    @classmethod
    def splitstring(cls, string):
        # splitter = string.split("-")
        # return cls(splitter[0], splitter[1], splitter[2], splitter[3])
        return cls(*string.split("-"))


Sheryl = Person("Sheryl", 25, 50000, "Python developer")
Abino = Person.splitstring("Abino-25-50000-Python developer")
Person.changeworkinghours(10)
print(Abino.printdetails())
print(Sheryl.printdetails())


class Programmer(Person):

    def __init__(self, name, age, salary, profession, language):
        super().__init__(name, age, salary, profession)
        self.language = language

    def printdetail(self):
        return f'Name is {self.name}, Age is {self.age}, Salary is {self.salary}, Profession is {self.profession},' \
               f'  language is {self.language}, Working {self.workinghours} hours a day'


Abiril = Programmer("Abiril", 5, 0, "developer", "python")
print(Abiril.printdetail())
