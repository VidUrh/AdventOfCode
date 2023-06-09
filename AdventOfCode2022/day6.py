f = open("day6.txt",'r')
line = f.readline()
buf = []
numChar = 14
for i,x in enumerate(line):
    buf.append(x)
    if len(buf)>numChar:
        buf = buf[1:]
    if len(set(buf)) == numChar:
        print(i+1)
        break