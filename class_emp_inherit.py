class Emp:

    def __init__(self, name, dept):
        self.name = name
        self.dept = dept
        print(f'{name} in {dept} is created.')

    def display(self):
        print(f'{self.name} works in {self.dept}')


class Accountant(Emp):
    def __init__(self, name, dept, acc_sys):
        super().__init__(name, dept)
        self.acc_sys = acc_sys

    def display(self):
        print(f'{self.name} works in {self.dept} following {self.acc_sys} standards.')


class Engineer(Emp):
    def __init__(self, name, dept, lang):
        super().__init__(name, dept)
        self.lang = lang

    def display(self):
        print(f'{self.name} works in {self.dept} programs in {self.lang}.')


e1 = Accountant('Alice', 'Accounting', 'GAAP')  # IFRS vs GAAP
e2 = Engineer('Eric', 'Engineering', 'Python')
e1.display()
e2.display()
