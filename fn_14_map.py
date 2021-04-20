a = ['1', '2', '3']
b = map(int, a)
print(list(b))

numbers = range(1, 11)
squares = map(lambda x: x**2, numbers)
print(list(squares))

