f=open("input.txt",'r')
lines=[x.strip('\n') for x in f.readlines()]
template = lines[0]
gr={}
for x in lines[2:]:
	comm=x.split(' -> ')
	gr[comm[0]]=comm[1]

for x in range(10):
	buf=template[0]
	for x in range(len(template)-1):
		if template[x]+template[x+1] in gr:
			buf+=(gr[template[x]+template[x+1]])
		buf+=template[x+1]
	template=buf

d = {x:template.count(x) for x in set(template)}
print("Part-1: "+str(max(d.values())-min(d.values())))


gr={}
for x in lines[2:]:
	comm=x.split(' -> ')
	gr[comm[0]]=[comm[0][0]+comm[1],comm[1]+comm[0][1]]

template=lines[0]

pairs={}
for k, v in zip(template, template[1:]):
	s = k + v
	if s not in pairs:
		pairs[s]=0
	pairs[s]+=1

count={x:template.count(x) for x in set(template)}
for i in range(40):
	newP={}
	for pair in pairs:
		a,b=gr[pair]
		c=pairs[pair]

		if a[1] not in count:
			count[a[1]]=0
		count[a[1]]+=c

		if a not in newP:
			newP[a]=0
		if b not in newP:
			newP[b]=0

		newP[a]+=c
		newP[b]+=c

	pairs=newP
temp=(sorted(count.values()))
print("Part-2: "+str(temp[-1]-temp[0]))
