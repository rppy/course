from functools import reduce


def add(a, b):
    return a + b


numbers = range(1, 101)
print(reduce(add, numbers))
