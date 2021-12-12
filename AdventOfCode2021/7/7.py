f=open("input.txt",'r')
lines=[int(x) for x in f.readline().split(',')];
lines.sort()
print(lines)
mini = float("inf");
c={x:lines.count(x) for x in set(lines)}
print(c)
el = sorted(list(set(lines)))
for x in el:
	ans=0
	for y in el:
		ans+=c[y]*sum(y for y in range(abs(y-x)+1))
	if ans<mini:
		mini=ans
	
print(mini)
