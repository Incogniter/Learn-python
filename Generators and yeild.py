import sys


# Python generators are a simple way of creating iterators. ... Simply speaking, a generator is a function that returns
# an object (iterator) which we can iterate over (one value at a time).
def my_range(n: int):
    print("my_range starts")
    start = 0
    while start < n:
        print("my_range is returning {}".format(start))
        yield start
        start += 1


big_range = range(5)
# big_range = my_range(5)
# _ = input("line 18")

print("big_range is {} bytes".format(sys.getsizeof(big_range)))

# create a list containing all the values in big_range
big_list = []

# _ = input("line 25")
for val in big_range:
    # _ = input("line 27 - inside loop")
    big_list.append(val)

print("big_list is {} bytes".format(sys.getsizeof(big_list)))
print(big_range)
print(big_list)

print("looping or not")
for i in big_range:
    print("i is {}".format(i))
