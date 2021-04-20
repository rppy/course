def div(x, y):
    return x / y


print(f'{div(3, 4) = }')  # positional argument
print(f'{div(y=3, x=4) = }')  # keyword argument


# enforcing positional / keyword parameters with / and *
def add(a, /, b, *, c):
    pass
    # argument a can be passed as positional only
    # argument b can be passed as positional or keyword argument
    # argument c can be passed as keyword only
    # otherwise exception is raised
