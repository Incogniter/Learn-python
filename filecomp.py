# compare file_for.py
print(__file__)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

number = int(input("please enter a number and ill tell u their square:"))

if number > 20:
    print("sorry the number is greater than the number expected")
else:

    squares = [number ** 2 for number in numbers]

    index_position = numbers.index(number)
    print(squares[index_position])
