i = [1, 2, 3]
while i != []:
    print(f'{i.pop() = }')

print()

# i is truthy until it becomes empty
i = [1, 2, 3]
while i:
    print(f'{i.pop() = }')


# falsy (False in the boolean context):
# False
# None
# 0
# 0.0
# 0j
# ""
# []
# {}
# set()
# ()
