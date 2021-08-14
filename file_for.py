# compare with filecomp
print(__file__)

numbers = [1, 2, 3, 4, 5, 6, 7]

number = int(input("please enter a number and ill tell u their square:"))

squares = []
for number in numbers:
    squares.append(number ** 2)

index_position = numbers.index(number)
print(squares[index_position])

# print(squares)
