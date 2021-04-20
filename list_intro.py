a = [1, 2, 3, 4, 5]
print(f'{a = }')

# can hold different types
a = [1, "Alice", 3, None, str]
print(f'{a = }')

# can hold lists
a = [[1, 2, 3], [4, 5, 6]]
print(f'{a = }')

# filling with the * operator
a = [0] * 10
print(f'{a = }')

# danger! this is not a 2d array
a = [[0] * 3] * 2
a[1][1] = 7
print(f'{a = }')
