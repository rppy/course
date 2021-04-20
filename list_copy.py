a = [10, 20, 30, 40, 50]
b = a
b[2] = 60
print(f'{a = }')

# shallow copies

# shallow copies: copy method
b = a.copy()
print(f'{b = }')

# shallow copies: any slice is a copy
b = a[:]
print(f'{b = }')

# shallow copies: copy module
from copy import copy
b = copy(a)
print(f'{b = }')

# deep copy - copies lists of lists
from copy import deepcopy
b = deepcopy(a)
print(f'{b = }')
