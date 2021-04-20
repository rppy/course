class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
        print(f'Creating {self.name} with age of {self.__age}')

    def greet(self):
        print(f'Hello {self.name} at age of {self.__age}')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if 0 < new_age < 120:
            self.__age = new_age
        else:
            print(f'Ignoring invalid age of {new_age}')


p = Person('Alice', 20)
p.greet()
p.age = -200
p.greet()
print(p.age)
