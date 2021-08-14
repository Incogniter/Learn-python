import timeit
import functools


def cal_vales(x, y: int):
    return x * y


numbers = [1, 2, 3, 4]
reduced_value = functools.reduce(cal_vales, numbers)
print(reduced_value)
print(sum(numbers))

result = 1
for x in numbers:
    result *= x
print(result)
