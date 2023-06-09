f = open("day8.txt",'r')
trees = [[int(a) for a in x.strip()] for x in f.readlines()]
n = len(trees)
m = len(trees[0])



def ff(x,y,startX,startY,direction=(0,0)):
    if x<0 or y<0 or y>m-1 or x>n-1:
        return 0
    if (trees[x][y]>=trees[startX][startY] and direction!=(0,0)):
        return 1
    else:
        if direction == (0,0):
            ena = ff(x+1,y,x,y,(1,0))
            dva = ff(x,y+1,x,y,(0,1))
            tri = ff(x-1,y,x,y,(-1,0))
            stiri = ff(x,y-1,x,y,(0,-1))
            if startX == x and startY == y:
                print(x,y,ena,dva,tri,stiri)
            return ena*dva*tri*stiri
        else:
            return ff(x+direction[0],y+direction[1],startX,startY,direction)+1


temp = [[0 for _ in range(m)] for _ in range(n)]
for x in range(n):
    for y in range(m):
        temp[x][y] = ff(x,y,x,y)
    
"""
visibles = set()

temp = [[0 for _ in range(m)] for _ in range(n)]
for x in range(n):
    maxi = -1
    for y in range(m):
        if trees[x][y] > maxi:
            maxi = trees[x][y]
            temp[x][y] = 1
            visibles.add((x,y))

for x in range(n):
    maxi = -1
    for y in range(m-1,-1,-1):
        if trees[x][y] > maxi:
            maxi = trees[x][y]
            temp[x][y] = 1
            visibles.add((x,y))

for y in range(m):
    maxi = -1
    for x in range(n):
        if trees[x][y] > maxi:
            maxi = trees[x][y]
            temp[x][y] = 1
            visibles.add((x,y))

for y in range(m):
    maxi = -1
    for x in range(n-1,-1,-1):
        if trees[x][y] > maxi:
            maxi = trees[x][y]
            temp[x][y] = 1
            visibles.add((x,y))
"""

[print(x) for x in temp]
print(max(x for y in temp for x in y))


