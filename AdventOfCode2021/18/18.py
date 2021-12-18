f=open("input.txt",'r')
lines=[x.strip('\n') for x in f.readlines()]
from collections import Counter
from itertools import combinations
from itertools import permutations


def d(suma):
	maxi=0
	c=0
	for x in suma:
		if x=='[':
			c+=1
		elif x==']':
			c-=1
		maxi=max(c,maxi)
	return maxi>4


def generirajVrstico(stack):
	temp=''.join(map(str,stack))
	buf=''
	for i in range(len(temp)-1):
		if temp[i+1].isdigit() and temp[i]!='[' or temp[i]==']' and temp[i+1]=='[' or temp[i].isdigit() and temp[i+1]=='[':
			buf+=temp[i]
			buf+=','
		else:
			buf+=temp[i]
	buf+=']'
	return eval(buf)


def generate(suma):
	temp=[]
	buf=''
	for x in suma:
		if x=='[':
			if len(buf):
				temp.append(int(buf))
				buf=''
			temp.append('[')
		elif x==']':
			if len(buf):
				temp.append(int(buf))
				buf=''
			temp.append(']')
		elif x==',':
			if len(buf):
				temp.append(int(buf))
				buf=''
		else:
			buf+=x

	return temp


def Reduce(suma):
	suma=suma.replace(' ','')
	suma=generate(suma)
	stack=[]
	depth=0
	x=0



	if not d(suma):
		return generirajVrstico(suma)

	while d(suma):
		depth=0
		x=0
		stack=[]
		while x<len(suma):
			temp=suma[x]
			if temp=='[':
				depth+=1
				stack.append('[')
			elif temp==']':

				stack.append(']')
				depth-=1
			elif temp==',':
				pass
			else:
				temp=int(temp)
				if depth>4:
					explode1=temp
					x+=1
					explode2=suma[x]
					for i in range(len(stack)-1,-1,-1):
						if isinstance(stack[i],int):
							stack[i]+=int(explode1)
							break
					for i in range(x+1,len(suma)):
						if isinstance(suma[i],int):
							suma[i]+=int(explode2)
							break
					stack.pop()
					stack.append(0)
					suma=stack+suma[x+2:]
					x=-1
					depth=0
					stack=[]
				else:
					stack.append(int(temp))
			x+=1

		depth=0
		x=0
		suma=stack
		stack=[]
		while x<len(suma):
			temp=suma[x]
			if temp=='[':
				depth+=1
				stack.append('[')
			elif temp==']':
				stack.append(']')
				depth-=1
			elif temp==',':
				pass
			else:
				temp=int(temp)
				if temp>9:
					split1=temp//2
					if temp%2:
						split2=temp//2+1
					else:
						split2=temp//2
					if depth==4:
						for i in range(len(stack)-1,-1,-1):
							if isinstance(stack[i],int):
								stack[i]+=int(split1)
								break
						for i in range(x+1,len(suma)):
							if isinstance(suma[i],int):
								suma[i]+=int(split2)
								break
						stack.append(0)
					else:
						stack.append('[')
						stack.append(split1)
						stack.append(split2)
						stack.append(']')


					suma=stack+suma[x+1:]
					depth=0
					x=-1
					stack=[]
					con=1
				else:
					stack.append(int(temp))
			x+=1







	return generirajVrstico(stack)


def dfs(root):
	if isinstance(root,int):
		return root
	else:
		return 3*dfs(root[0])+2*dfs(root[1])

start = lines[0]
start = Reduce(start)

for x in lines[1:]:
	num=Reduce(str(x))
	suma='['+str(start)+','+str(num)+']'
	start = Reduce(suma)

print("Part-1:",dfs(start))
maxi=0
reduced={x:Reduce(x) for x in lines}
for prvi in lines:
	for drugi in lines:
		if prvi==drugi:
			continue
		else:
			string = '['+str(reduced[prvi])+','+str(reduced[drugi])+']'
			maxi=max(dfs(Reduce(string)),maxi)

print("Part-2:",maxi)
