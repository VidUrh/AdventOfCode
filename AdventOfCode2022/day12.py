f = open("day12.txt",'r')


lines = [[ord(a) for a in x.strip()] for x in f.readlines()]

yStart,xStart = 0,0
yEnd,xEnd = 0,0

for i,x in enumerate(lines):
    for j,y in enumerate(x):
        if y == 83:
            yStart = j
            xStart = i
            lines[i][j] = 97
        if y == 69:
            yEnd = j
            xEnd = i
            lines[i][j] = 122

n,m = len(lines),len(lines[0])
queue = [(xEnd,yEnd,0)]
visited = []

#[print(a) for a in lines]
temp = [[' ' for _ in range(m)] for _ in range(n)]
while len(queue)>0:
    x,y,depth = queue.pop(0)
    if (x,y) in visited:
        continue
    visited.append((x,y))
    print(x,y)
    if lines[x][y]==97:
        print(depth)
        break
    else:
        if x>0 and (lines[x-1][y]-lines[x][y])>-2:
            queue.append((x-1,y,depth+1))
        
        if y>0 and lines[x][y-1]-lines[x][y]>-2:
            queue.append((x,y-1,depth+1))
        
        if x<n-1 and lines[x+1][y]-lines[x][y]>-2:
            queue.append((x+1,y,depth+1))
        
        if y<m-1 and (lines[x][y+1]-lines[x][y])>-2:
            queue.append((x,y+1,depth+1))
    temp[x][y]='#'
with open("temp.txt",'w') as bc:
    [bc.write(''.join(x)+'\n') for x in temp]