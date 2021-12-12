asdf = open("1.dan.txt")
fuel = [int((int(line)/3))-2 for line in asdf]
enz = sum(fuel)

#----------------------
i = 0
#print(fuel)
try:
    while True:
        line = fuel[i]
        a = int((int(line)/3))-2
        if a < 0:
            i+=1
        else:
            fuel.append(a)
            i+=1
            
except IndexError:
    pass
print(sum(fuel))





'''benz = fuel.append([int((int(line)/3))-2 for line in fuel])
print(benz)
def benzin(benz):
    ben = int((int(benz)/3))-2
    if ben < 0:
        print(sum(t))
        return sum(t) 
    else:
        t.append(ben)
        benzin(ben)
c = []
for asd in fuel:
    print(benzin(asd))
    c.append('a')
    t = []
print(c)


#m = sum(c)

#print(m + enz)
'''
