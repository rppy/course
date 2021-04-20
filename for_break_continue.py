# for + break
fruits = ['apple', 'banana', 'orange', 'pear']
for fruit in fruits:
    if fruit.startswith('o'):
        print(f'Found: {fruit}')
        break
print('end')

print()

# for + continue
for fruit in fruits:
    if fruit.startswith('o'):
        continue
    print(f'Fruit: {fruit}')
print('end')

print()

# for + break + else
for fruit in fruits:
    if fruit.startswith('x'):
        print(f'Found: {fruit}')
        break
else:
    print('No such fruit')
print('end')
