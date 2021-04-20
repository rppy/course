# read line by line

with open('file.txt') as fh:
    for line in fh:
        print(line.strip('\n'))

