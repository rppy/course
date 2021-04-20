class Person:
    def __init__(self, name, height=170):
        self.name = name
        self.height = height

    def greet(self):
        print(f'Hello {self.name}')

    def __str__(self):
        return f'{self.name} who is {self.height} tall.'

    def __repr__(self):
        return f'Person("{self.name}", {self.height})'

    def __eq__(self, other):
        return (self.name, self.height) == (other.name, other.height)

    def __len__(self):
        return self.height



p = Person('Alice')
print(p.name)
p.greet()
print(p)
print(repr(p))

p2 = Person('Alice', 170)

print(f'{p == p2}')

print(f'{len(p)}')
