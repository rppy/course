class FlexInt:
    def __init__(self, value):
        self.value = int(value)

    def __str__(self):
        return str(self.value)

    def __add__(self, other):
        return self.value + other.value

    # def __add__(self, other):  # FlexInt Type
    #     return FlexInt(self.value + other.value)
    #
    # def __add__(self, other):  # FlexInt + int/str works
    #     if hasattr(other, 'value'):
    #         return FlexInt(self.value + other.value)
    #     else:
    #         return FlexInt(self.value + int(other))
    #
    # def __radd__(self, other):  # right add with int/str
    #     return FlexInt(self.value + int(other))


a = FlexInt(5)
b = FlexInt(6)

print(type(a).__name__, a)
print(type(b).__name__, b)
print(type(a + b).__name__, a + b)
