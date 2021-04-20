import traceback

d = {}
try:
    n = d['a']
except Exception as err:
    print("An error occurred:", err)
    print("An error occurred:", type(err).__name__, err)
    #traceback.print_exc()
    print(traceback.format_exc())

