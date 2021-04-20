def some_function():
    if True:
        raise ValueError('Details of the error...')


try:
    print('start')
    some_function()
    print('end')
except Exception as err:
    print("An error occurred:", type(err).__name__, err)
