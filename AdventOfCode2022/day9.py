f = open("day9.txt",'r')
lines = f.readlines()
size = 1000
polje = [[0 for _ in range(size)] for _ in range(size)]


xHead = size//2
yHead = size//2
xTail = size//2
yTail = size//2
polje[xHead][yHead] = 1


[print(x) for x in polje]


def MoveHead(smer):
    global xHead
    global yHead
    global polje
    xHead+=smer[0]
    yHead+=smer[1]

def MoveTail(smer):
    global xHead
    global yHead
    global xTail
    global yTail
    global polje

    a = xTail>xHead+1
    b = xTail<xHead-1
    c = yTail>yHead+1
    d = yTail<yHead-1
    

    if any((a,b,c,d)):

        a = xTail>xHead
        b = xTail<xHead
        c = yTail>yHead
        d = yTail<yHead
        if a:
            xTail-=1
        if b:
            xTail+=1
        if c:
            yTail-=1
        if d:
            yTail+=1

    #print(xTail,yTail)    
    polje[xTail][yTail] = 1


for x in lines:
    komanda,koliko = x.split()
    if komanda == 'R':
        smer = (0,1)
    elif komanda == 'U':
        smer = (-1,0)
    elif komanda == 'L':
        smer = (0,-1)
    else:
        smer = (1,0)
    for x in range(int(koliko)):
        MoveHead(smer)
        MoveTail(smer)
        #print(10*'-------')
        #[print(x) for x in polje]
        #input()

print(sum(x for y in polje for x in y))