from collections import Counter

f = open("day3.txt")

lines = [x.strip('\n') for x in f.readlines()]

val=0

for group in range(0,len(lines),3):
    ekipe = lines[group:group+3]
    ena = set(ekipe[0])
    dva = set(ekipe[1])
    tri = set(ekipe[2])
    c = ena.intersection(dva).intersection(tri)
    print(c)
    for x in c:
        if x.isupper():
            val+=ord(x)-64+26
        elif x.islower():
            val+=ord(x)-96
print(val)