# tuples are immutable, hence hashable

t = (5, 6)
print(f'{t = }')
print(f'{hash(t) = }')

# dict keys may be anything that is hashable
d = {}
for i in range(1, 11):
    for j in range(1, 11):
        d[(i, j)] = i * j
print(d)
