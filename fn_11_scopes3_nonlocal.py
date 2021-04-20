x = 5


def hello():
    x = 15

    def inner():
        nonlocal x
        x = 1
        print('in inner', x)

    inner()
    print('in hello', x)


hello()
print('in main', x)

