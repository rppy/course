# read line by line

fh = open('file.txt')
for line in fh:
    print(line.strip('\n'))
fh.close()

