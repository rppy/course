s = set()
print(f"{s = }")
print(f"{type(s) = }")

s = {1, 2, 3, 4}
print(f"{s = }")
print(f"{type(s) = }")

d = {}  # dict!
print(f"{d = }")
print(f"{type(d) = }")

friends = {'Alice', 'Bob', 'Charlie'}
print(f"{friends = }")

friends.add('David')
friends.add('Alice')

print(f"{friends = }")

friends.remove('Bob')  # KeyError if key not present
friends.discard('Bob')  # silent if key not present
print(f"{friends = }")

print(f"{'Alice' in friends = }")
