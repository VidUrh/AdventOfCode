f=open("input.txt",'r')
lines=[x.strip('\n').split('->') for x in f.readlines()]
lines=[[[int(x) for x in i.split(',')] for i in y] for y in lines]
flat = [x for y in lines for x in y]
flat = [x for y in flat for x in y]
print(flat)
maxnum=max(flat)
grid = [[0 for x in range(maxnum+1)]for x in range(maxnum+1)]

maxi=0
for x in lines:
	if(x[0][0]==x[1][0]):
		print(x)
		for i in range(min(x[0][1],x[1][1]),max(x[0][1],x[1][1])+1):
			grid[x[0][0]][i]+=1
			maxi=max(grid[x[0][0]][i],maxi)
	elif (x[0][1]==x[1][1]):
		for i in range(min(x[0][0],x[1][0]),max(x[0][0],x[1][0])+1):
			grid[i][x[0][1]]+=1
			maxi=max(grid[i][x[0][1]],maxi)
	else:
		temp=[x[0][0],x[0][1]]
				
		if(x[0][0]<x[1][0]):
			if(x[0][1]<x[1][1]):
				while temp!=x[1]:
					print(temp)
					grid[temp[0]][temp[1]]+=1
					temp[0]+=1
					temp[1]+=1

				grid[temp[0]][temp[1]]+=1
			else:			
				while temp!=x[1]:
					
					print(temp)
					grid[temp[0]][temp[1]]+=1
					temp[0]+=1
					temp[1]-=1
				
				grid[temp[0]][temp[1]]+=1
		else:
		
		
			if(x[0][1]<x[1][1]):
				while temp!=x[1]:
					grid[temp[0]][temp[1]]+=1
					temp[0]-=1
					temp[1]+=1
			
				grid[temp[0]][temp[1]]+=1
			else:			
				while temp!=x[1]:
					print(temp,x[1])
					grid[temp[0]][temp[1]]+=1
					temp[0]-=1
					temp[1]-=1
				
				grid[temp[0]][temp[1]]+=1

print(maxi)
for x in zip(*grid):
	print(x)
print(sum(1 for x in [i for y in grid for i in y] if x>1))

