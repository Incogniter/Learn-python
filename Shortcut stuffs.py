class Person:
    workinghours = 8

    def __init__(self, name, age, salary, profession):
        self.name = name
        self.age = age
        self. salary = salary
        self.profession = profession

    def printdetails(self):
        return f'Name is {self.name}, Age is {self.age}, Salary is {self.salary}, Profession is {self.profession},' \
               f' Working {self.workinghours} hours a day'

    # ro add sheryl +abino
    def __add__(self, other):
        return self.salary - other.salary

    # to subtract sheryl - abino

    def __sub__(self, b):
        return self.age + b.age

    # to make the whole detail to print
    def __str__(self):
        return f'Name is {self.name}, Age is {self.age}, Salary is {self.salary}, Profession is {self.profession},' \
               f' Working {self.workinghours} hours a day'

    def __repr__(self):
        return f'Name is {self.name}, Age is {self.age}, Salary is {self.salary}, Profession is {self.profession},' \
               f' Working {self.workinghours} hours a day'


Sheryl = Person("Sheryl", 25, 750000, "Python developer")
Abino = Person("Abino", 25, 50000, "Python developer")

# to make this salry to add see above
print(Sheryl - Abino)
print(Sheryl + Abino)

print("_"*50)
# print(Abino.printdetails())
# print(Sheryl.printdetails())
print(Abino) # output uses __str__(self) to get output
