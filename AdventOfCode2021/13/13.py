f=open("input.txt",'r')
lines = [x.strip('\n') for x in f.readlines()]
coor=[]
for i,line in enumerate(lines):
	if(line==''):
		instr = lines[i+1:]
		break
	x,y=map(int,line.split(','))
	coor.append((x,y))
dimenX=max([x[0] for x in coor])
dimenY=max([x[1] for x in coor])
grid = [['.' for x in range(dimenX+1)] for y in range(dimenY+1)]
for c in coor:
	grid[c[1]][c[0]]='#'

counter=0
for x in instr:
	comm=x.split()
	comm=comm[2]
	kako,kje=comm.split('=')
	kje=int(kje)
	if kako == 'y':
		zgorej=grid[:kje]
		spodej=grid[kje+1:][::-1]
		merged=[]
		if(len(zgorej)<len(spodej)):
			for k in range(len(spodej)-len(zgorej)):
				print(k)
				merged.append(spodej[k])
			for i in range(min(len(zgorej),len(spodej))):
				merged.append(['#' if zgorej[i][a]=='#' or spodej[i][a]=='#' else ' ' for a in range(len(zgorej[0]))])
		else:
			temp=len(zgorej)-len(spodej)
			for k in range(temp):
				merged.append(zgorej[k])
			for i in range(min(len(zgorej),len(spodej))):
				merged.append(['#' if zgorej[i+temp][a]=='#' or spodej[i][a]=='#' else ' ' for a in range(len(zgorej[0]))])



		grid=merged

	else:
		levo = [a[:kje] for a in grid]
		desno=[a[kje+1:][::-1] for a in grid]

		merged=[]
		for i in range(len(grid)):
			merged.append(['#' if levo[i][a]=='#' or desno[i][a]=='#' else ' ' for a in range(len(levo[0])) ])
		grid=merged
	if(counter==0):
		print("Part-1: "+ str(sum(1 for a in [x for y in grid for x in y] if a=='#')))
		counter+=1

print("Part-2: ")
for a in grid:
	print(''.join(a))




