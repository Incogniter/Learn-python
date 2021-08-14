entries = [1, 2, 3, 4, 5]

print("all: {}".format(all(entries)))
print("any: {}".format(any(entries)))

print("iterable with false value")
# zero id odd here
enteriess = [1, 2, 0, 4, 5]

print("all: {}".format(all(enteriess)))
print("any: {}".format(any(enteriess)))

print("-"*50)

entries = []
print("all: {}".format(all(entries)))
print("any: {}".format(any(entries)))

