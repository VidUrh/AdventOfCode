f = open("input.txt",'r');

lines = [x.strip('\n') for x in f.readlines()];
lines = [[x.split()[0],x.split()[1]] for x in lines]

preskok=0

for x in lines[::-1]:
	if(x[0]=='jmp'):
		if(int(x[1])<0):
			break
	preskok+=1
	print(x)


preskok=len(lines)-preskok-1
print(preskok)	

acc=0;
executing = 0;
visited=[False for _ in lines]


while not visited[executing]:
	visited[executing] = True;
	temp = lines[executing]
	ukaz,koliko = temp;
	if ukaz=='nop':
		if(int(executing+int(koliko)))>=preskok:
			print(temp)







	
acc=0;
executing = 0;
visited=[False for _ in lines]


while not visited[executing]:
	visited[executing] = True;
	temp = lines[executing]
	ukaz,koliko = temp;
	if(ukaz=='acc'):
		acc=int(eval(str(acc)+koliko))
		executing+=1
	elif ukaz == 'jmp':
		executing = int(eval(str(executing)+koliko))
	else:
		executing+=1

