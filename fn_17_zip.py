names = ['Alice', 'Bob', 'Charlie']
ages = [20, 25, 30]

pairs = zip(names, ages)
pairs = list(pairs)

print(pairs)

print(list(zip(*pairs)))

