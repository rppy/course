def add(*args):
    print(args)
    return sum(args)


print(f'{add(4, 5, 6) = }')
