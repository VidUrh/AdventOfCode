file = open("input.txt",'r');
lines = file.readlines()
nums=lines[0]
boardlines = lines[2:]

kdaj={}
numbers=nums.strip("\n").split(',')
print(numbers)
for i,x in enumerate(numbers):
	kdaj[int(x)]=i


boards=[]
buf=[]

for x in boardlines:
	if x=='\n':
		boards.append(buf)
		buf=[]
	else:
		buf.append([int(i) for i in x.split()])
	
boards.append(buf)

mintime=[0,-1]

for num,board in enumerate(boards):

	vrstica=float("inf")
	stolpec=float("inf")
	
	for i in range(5):
		time=max(kdaj[x] for x in board[i])
		vrstica=min(time,vrstica)
		times=max(kdaj[x] for x in [y[i] for y in board])
		stolpec=min(times,stolpec)
	mini = min(stolpec,vrstica)
	print(mini)
	if(mintime[0]<mini):
		mintime=[mini,num]

print(mintime)

izvlecene=[int(x) for x in numbers[:mintime[0]+1]]
zmagovalna = boards[mintime[1]]
print(izvlecene)
print(zmagovalna)

zmagovalna = [x for y in zmagovalna for x in y]


for i in izvlecene:
	zmagovalna=[x for x in zmagovalna if x!=i]
	
print((zmagovalna))
print(izvlecene)

print(sum(zmagovalna)*izvlecene[-1])




















