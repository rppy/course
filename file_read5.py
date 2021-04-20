fh = open('file.txt')
while True:
    line = fh.readline()
    if not line:
        break
    print(line)
fh.close()
