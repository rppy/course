x = 5


def hello():
    global x
    print('in hello', x)
    x = 1
    print('in hello', x)


hello()
print('in main', x)
