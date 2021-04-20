s = 'alice bob charlie david'
print(f'{s = }')
print(f'{s.count(" ") = }')  # 3
print(f'{s.split(" ") = }')  # ['alice', 'bob', 'charlie', 'david']
print()

a = ['alice', 'bob', 'charlie', 'david']
print(f'{a = }')
print(f'{"-".join(a) = }')  # 'alice-bob-charlie-david'
print()

print(f'{s.lower() = }')  # 'alice bob charlie david'
print(f'{s.upper() = }')  # 'ALICE BOB CHARLIE DAVID'
print(f'{s.capitalize() = }')  # 'Alice bob charlie david'
print(f'{s.title() = }')  # 'Alice Bob Charlie David'
print()

print(f'{s.startswith("a") = }')  # True
print(f'{s.index("i") = }')  # ValueError if not found
print(f'{s.find("i") = }')  # -1 if not found
print(f'{s.replace("li", "XX") = }')
print()

print(f'{"12".zfill(8) = }')  # '00000012'
print()

b = s.encode('utf-8')
print(f'{b = }')  # b'alice bob charlie david'
s = b.decode('utf-8')
print(f'{s = }')  # 'alice bob charlie david'
