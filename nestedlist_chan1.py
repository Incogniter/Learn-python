# chalenge using multiplication table

for i in range(1, 11):
    for j in range(1, 11):
        print(i, i * j)
print("-"*40)

times = [(i, i* j) for i in range(1, 11) for j in range(1, 11)]
print(times)
print("-"*40)

for x, y in [(i, i* j) for i in range(1, 11) for j in range(1, 11)]:
    print(x, y)
print("-"*40)

times2 = [[(i, i* j) for i in range(1, 11)] for j in range(1, 11)]
print(times2)
print("-"*40)

for x, y in ((i, i* j) for i in range(1, 11) for j in range(1, 11)):
    print(x, y)




