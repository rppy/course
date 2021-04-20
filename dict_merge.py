x = {'a': 1, 'b': 2}
y = {'c': 3, 'd': 4}
print(f"{x = }, {y = }")

m = x.copy()
m.update(y)
print(f"{m = }")

m = {**x, **y}  # Py 3.5
print(f"{m = }")

m = x | y  # Py 3.9
print(f"{m = }")
