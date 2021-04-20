numbers = range(1, 11)

even = lambda x: x % 2 == 0
results = filter(even, numbers)
print(list(results))

