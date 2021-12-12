f = open("input.txt",'r');
lines = [x.strip('\n') for x in f.readlines()]

ans=0
anss=[]
for line in lines:
	stack=[]
	for y in line:
		if y in '([{<':
			stack.append(y)
		else:
			m=stack.pop()
			if(m!='[' and y==']'):
				stack=[]
				ans+=57
				break
			if(m!='(' and y==')'):
				ans+=3
				stack=[]
				break
			if(m!='<' and y=='>'):
				stack=[]
				break
				ans+=25137
			if(m!='{' and y=='}'):
				ans+=1197
				stack=[]
				break

	ans=0
	if(len(stack))>0:
		for x in stack[::-1]:
			ans*=5
			ans+='([{<'.index(x)+1
		anss.append(ans)
		print(line,stack[::-1],ans)

print(ans)
anss.sort()
print(anss)
print(anss[len(anss)//2])
