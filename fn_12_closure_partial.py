from functools import partial


def power(base, exponent):
    return base ** exponent


square = partial(power, exponent=2)

print('power:', power(3, 2))
print('power:', square(3))

