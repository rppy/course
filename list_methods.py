a = [1, 2, 3, 4, 5]

print(f'{a = }')

a.append(6)
print(f'{a = }')

a.insert(3,7)
print(f'{a = }')

a.extend([1, 2, 3])
print(f'{a = }')

a.pop(0)
print(f'{a = }')

a.pop(-1)
print(f'{a = }')

a.count(2)
print(f'{a = }')

a.index(5)
print(f'{a = }')

a.remove(4)
print(f'{a = }')

a.reverse()  # in place
print(f'{a = }')

a.sort()  # in place
print(f'{a = }')
