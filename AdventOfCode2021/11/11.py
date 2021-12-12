f=open("input.txt",'r');
lines=[x.strip('\n') for x in f.readlines()];

matrix=[[0 for x in range(len(lines[0])+2)]]
for x in lines:
	matrix.append([0]+[int(y) for y in x]+[0])


matrix.append([0 for x in range(len(lines[0])+2)])
print(matrix)


ans=0


while True:

	for i,x in list(enumerate(matrix))[1:len(matrix)-1]:
		for j,y in list(enumerate(x))[1:len(x)-1]:
			matrix[i][j]+=1
	t=True

	flashed=[]
	while t:
		t=False
		for x,i in list(enumerate(matrix))[1:len(matrix)-1]:
			for y,j in list(enumerate(i))[1:len(i)-1]:
				if(j>9):
					t=True
					matrix[x][y]=0
					matrix[x+1][y+1]+=1
					matrix[x+1][y]+=1
					matrix[x+1][y-1]+=1
					matrix[x][y+1]+=1
					matrix[x][y-1]+=1
					matrix[x-1][y+1]+=1
					matrix[x-1][y]+=1
					matrix[x-1][y-1]+=1
					flashed.append((x,y))

	for i,j in flashed:
		matrix[i][j]=0
	if(len(flashed)==100):
		print(ans)
		break

	ans+=1








