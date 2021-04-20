x = {'a', 'b', 'c'}
y = {'c', 'd', 'e'}
print(f"{x = }, {y = }")

u = x | y
print(f"{u = }")
u = x.union(y)
print(f"{u = }")

i = x & y
print(f"{i = }")
i = x.intersection(y)
print(f"{i = }")

d = x - y
print(f"{d = }")
d = x.difference(y)
print(f"{d = }")

sd = x ^ y
print(f"{sd = }")
sd = x.symmetric_difference(y)
print(f"{sd = }")