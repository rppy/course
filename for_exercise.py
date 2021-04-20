# iterate through letters/words/lines
text = """this is the first row
this is the second one
and finally the last row"""

# iterate through letters:
for i in text:
    print(i)

print()

# iterate through words:
for i in text.split():
    print(i)

print()

# iterate through lines:
for i in text.split('\n'):
    print(i)
