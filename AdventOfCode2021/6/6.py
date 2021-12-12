f=open("input.txt",'r')
fish=[int(x) for x in f.readline().split(',')];
c={x:fish.count(x) for x in range(9)}
print(c)
ans=sum(c.values())
for x in range(256):
	temp=c[0]
	for x in range(8):
		c[x]=c[x+1]
	c[6]+=temp
	c[8]=temp
	ans+=temp
	print(c)
print(ans)
