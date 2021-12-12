def ff(x,y,i):
	if x<0 or y<0 or x>len(matrix)-1 or y>len(matrix[0])-1:
		return 0
	elif matrix[x][y]==9:
		return 0
	elif matrix[x][y]>=i:
		matrix[x][y]=9
		return 1+ff(x+1,y,i+1)+ff(x-1,y,i+1)+ff(x,y-1,i+1)+ff(x,y+1,i+1)
	else:
		return 0

f = open("input.txt",'r');
lines = [x.strip('\n') for x in f.readlines()]
matrix=[]
for x in lines:
	matrix.append([int(y) for y in x])

ans=0
sizes=[]
for i,x in enumerate(matrix):
	
	
	for j,y in enumerate(x):
		if((i-1<0 or matrix[i-1][j]>y) and (i+1>len(matrix)-1 or matrix[i+1][j]>y) and (j+1>len(matrix[0])-1 or matrix[i][j+1]>y) and (j-1<0 or matrix[i][j-1]>y)):
			sizes.append(ff(i,j,y))
			ans+=y+1
sizes.sort(reverse=True)
print(matrix)
print(sizes[0]*sizes[1]*sizes[2])
