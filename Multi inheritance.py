# multi inheritance

class Person:

    var = 1

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


class Player:

    var = 2
    no_of_games = 4

    def __init__(self, name, game):
        self.name = name
        self.game = game


abino = Player("Abino", "Hand Ball")


class Coolprogramer(Person, Player):

    var = 3
    pass


robilin = Coolprogramer("Robilin", 5000000000000000000000000000000000000, "B.E,M.E,PHD,Doctrate", "developer")
print(robilin.var)
