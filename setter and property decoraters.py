class Employee:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    @property   # decorator to run as a artribute changes its method
    def email(self):

        if self.firstname is None or self.lastname is None:
            return "email is not set"
        return f'{self.firstname}{self.lastname}@gmail.com'

    @email.setter
    def email(self, string):
        name = string.split('@')[0]
        self.firstname = name.split('.')[0]
        self.lastname = name.split('.')[1]

    @email.deleter
    def email(self):
        self.firstname = None
        self.lastname = None

    def explain(self):
        return f'This employee name is {self.firstname} {self.lastname}'


abino = Employee("Abino", "Robilin")
print(abino.firstname)
print(abino.lastname)
print(abino.explain)
print(abino.explain())
abino.firstname = "abirl"
print(abino.email)

abino.email = "abino.robilin@gmail.com"
print(abino.email)
print(abino.firstname)
print(abino.lastname)

del abino.email
print(abino.email)
