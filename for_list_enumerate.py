# iterating through a list by items
for item in ['apple', 'banana', 'pear']:
    print(item)

print()

# iterating through a list by index
fruits = ['apple', 'banana', 'pear']
for index in range(len(fruits)):
    print(f'{index}. fruit is {fruits[index]}')

print()

# enumerate to get item and index
fruits = ['apple', 'banana', 'pear']
for index, fruit in enumerate(fruits):
    print(f'{index}. fruit is {fruit}')
