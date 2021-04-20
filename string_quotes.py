a = "this is a text"  # double quotes
b = 'this is also'  # single quotes
print(f'a: {a}')
print(f'b: {b}')
print(f'a+b: {a+b}')  # concatenation

c = """multi
line
text"""
print(f'c: {c}')  # multiline

d = "some " \
    "long " \
    "text"

e = "some \
long \
text"
print(f'd: {d}')  # single line
print(f'e: {e}')  # single line
