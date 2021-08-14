#multi level inheritance

class Husband:
    freelancer = 20000

    def freelancing(self):
        return f"he is a well freelancer ,and she works well and earns rupees {self.freelancer}"
    pass


class Wife(Husband):
    pass


class Child(Wife):
    dancing = 20

    def dancer(self):
        return f"i am a folk dancer, my dancing skill {self.dancing}"

    pass


abino = Husband()
sheryl = Wife()
abiryl = Child()
print(sheryl.freelancing())
