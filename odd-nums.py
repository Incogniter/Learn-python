def odd_numbers():
    n = 1
    while True:
        yield n
        n = n+2

# odd = odd_numbers()
# odd numbers till 100
# for i in range(100):
#     print(next(odd))
# to find pi value as 3.14159
def pi_search():
    odd = odd_numbers()
    approximation = 0
    while True:
        approximation += (4 / next(odd))
        yield approximation
        approximation -= (4 / next(odd))
        yield approximation

approx_pi = pi_search()

for i in range(100):
    print(next(approx_pi))