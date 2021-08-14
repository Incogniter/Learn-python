class Kettle(object):
    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

# setting new value for kenwood
kenwood.price = 12.95
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.99)
print("Models: {} = {}\n{} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))
print("Models: {0.make} = {0.price}\n{1.make} = {1.price}".format(kenwood, hamilton))

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

Kettle.switch_on(kenwood)
print(kenwood.on)
print("= "*100)
kenwood.power = 1.5
print(kenwood.power)
# print(hamilton.power)

print("switch to atomic")
Kettle.power_source = "Atomic"
print(Kettle.power_source)
print("switch to gas")
kenwood.power_source = "gas"
print(kenwood.power_source)
print(hamilton.power_source)
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)
