class Emp:
    count = 0

    def __init__(self, name, dept):
        self.name = name
        self.dept = dept
        self.__class__.count += 1
        print(f'{name} in {dept} is created.')

    @classmethod
    def show_count(cls):
        print(f'Emp count: {cls.count}')

    @staticmethod
    def annual_salary_bump(salary):
        return salary * 1.1


# e1 = Emp('Alice', 'Accounting')
# print(e1.name)
# e2 = Emp('Bob', 'Booking')
# Emp.show_count()
# print(f'{e2.annual_salary_bump(1000) = }')

# I.C.P.O.

