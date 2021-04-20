from functools import reduce

numbers = [1, 5, 6, 3, 2]
print(reduce(lambda x, y: x if x > y else y, numbers))
