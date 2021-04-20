def power(exponent):
    def inner(base):
        return base ** exponent
    return inner


square = power(2)
cube = power(3)

print(square(2))
print(cube(2))

print(square(3))
print(cube(3))

