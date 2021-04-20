# list comprehension
a = [1, 2, 3, 4, 5, 6]
print(f'{a = }')

b = [i for i in a]
print(f'{b = }')

b = [i ** 2 for i in a]
print(f'{b = }')

b = [i for i in a if i % 2 == 0]
print(f'{b = }')

b = [i ** 2 for i in a if i % 2 == 0]
print(f'{b = }')
