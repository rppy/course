d = {'name': 'Alice', 'age': 20, 'nat': 'US'}
print(f"{d = }")

print()

print(f"{d.keys() = }")
print(f"{d.values() = }")
print(f"{d.items() = }")

print()

for key in d:
    print(f'Key: {key}, Value: {d[key]}')

print()

for key, value in d.items():
    print(f'Key: {key}, Value: {value}')

print()

print(f"{d.get('name') = }")
print(f"{d.get('birthday') = }")
print(f"{d.get('birthday', 'No such data.') = }")

print()

print(f"{d.pop('age') = }")
print(f"{d = }")
# d.pop('birthday')  # KeyError