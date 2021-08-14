list = [i for i in range(100) if i % 3 == 0]
print(list)

dict = {i: f'item{i}' for i in range(100)}
print(dict)

dict1 = {value: key for key, value in dict.items() }
print(dict1)