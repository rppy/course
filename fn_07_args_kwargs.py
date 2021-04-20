
def add(*args, **kwargs):
    print(type(args), args)
    print(type(kwargs), kwargs)
    return sum(args) + sum(kwargs.values())


print(f'{add(1, 2, 3, first=4, second=5, third=6) = }')
