def add(a, b):
    return a+b


def sub(a, b):
    return a-b


functions = [add, sub]


for function in functions:
    result = function(3, 4)
    print(f'{result = }')
