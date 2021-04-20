x = 5
y = 0
try:
    z = x / y
except TypeError as err:
    print('number expected!')
except ZeroDivisionError as err:
    print('cannot divide with zero!')
except Exception as err:
    print('unknown error!')
else:
    print('no exception occurred')
    print(z)
finally:
    print('ending clause')
