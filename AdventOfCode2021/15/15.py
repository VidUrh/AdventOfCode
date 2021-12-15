from collections import Counter
from itertools import permutations as perm
from itertools import combinations as comb


f=open("input.txt",'r')
lines=[x.strip('\n') for x in f.readlines()]
matrix=[]
for x in lines:
	matrix.append([int(y) for y in x])



dp=[[0 for _ in range(len(matrix[0]))] for _ in matrix]
for x in dp:
	x.append(float("inf"))
dp.append([float("inf") for x in range(len(matrix[0])+1)])
dp[-1][-1]=matrix[-1][-1]
for x in range(len(matrix)-1,-1,-1):
	for y in range(len(matrix[0])-1,-1,-1):
		if x==len(matrix)-1 and y==len(matrix[0])-1:
			continue
		prvi=dp[x+1][y]+matrix[x][y]
		drugi=dp[x][y+1]+matrix[x][y]
		dp[x][y]=min(prvi,drugi)


print("Part-1: "+ str(dp[0][0]))


newM=[x for x in matrix]
for i in range(4):
	for x in range(len(matrix)):
		newM.append([a+i+1 if a+i+1<=9 else (a+i+1)%9 for a in matrix[x]])


matrix=[[a for a in x] for x in newM]


for i in range(4):
	for x in range(len(matrix)):
		vrstica=[a+i+1 if a+i+1<=9 else (a+i+1)%9 for a in newM[x]]
		[matrix[x].append(a) for a in vrstica]



dp=[[0 for _ in range(len(matrix[0]))] for _ in matrix]
for x in dp:
	x.append(float("inf"))
dp.append([float("inf") for x in range(len(matrix[0])+1)])
dp[-1][-1]=matrix[-1][-1]
for x in range(len(matrix)-1,-1,-1):
	for y in range(len(matrix[0])-1,-1,-1):
		if x==len(matrix)-1 and y==len(matrix[0])-1:
			continue
		prvi=dp[x+1][y]+matrix[x][y]
		drugi=dp[x][y+1]+matrix[x][y]
		dp[x][y]=min(prvi,drugi)


print("Part-2: "+ str(dp[0][0]))










