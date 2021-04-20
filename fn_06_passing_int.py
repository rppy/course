x = 300
print(id(x))

def modify(y):
    print(id(y))
    y = 400


modify(x)
print(x)
