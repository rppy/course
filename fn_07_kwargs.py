def add(**kwargs):
    print(kwargs)
    return sum(kwargs.values())


print(f'{add(first=4, second=5, third=6) = }')
