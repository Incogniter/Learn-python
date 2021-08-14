class A:
    classvar1 = "I am a class variable in class A"

    def _init_(self):
        self.var1 = "i am inside the  constructer of class A"
        self.classvar1 = "i am inside the contructer of class A1"
        self.special = "special"


class B(A):
    classvar1 = "I am a class variable in class A"

    def _init_(self):
        # if u need special in 'class A' use this
        super()._init_()
        self.var1 = "i am a class variable in class B"
        self.classvar1 = "i am inside the contructer of class B"


a = A()
b = B()
# print(b.var1)
print(b.classvar1)
print(b.special)
