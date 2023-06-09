f = open("day4.txt")

lines = [x.strip('\n') for x in f.readlines()]

v = 0
for pair in lines:
    e,d = pair.split(',')
    start1,end1 = map(int,e.strip().split('-'))
    start2,end2 = map(int,d.strip().split('-'))
    
    if (end1>=start2 and start1<=start2) or (end2>=start1 and start2<=start1):
        v+=1
        print(start1,end1,start2,end2)
print(v)