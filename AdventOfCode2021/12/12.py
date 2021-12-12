f=open("input.txt","r");
lines = [x.strip('\n') for x in f.readlines()]
graph = {}
for x in lines:
	a,b = x.split('-')
	if a not in graph:
		graph[a]=[]
	if b not in graph:
		graph[b]=[]
	graph[a].append(b)
	graph[b].append(a)
visited = {x:0 for x in graph.keys() if x==x.lower()}
ans=set()
def dfs(root,visited,path):
	if root=='end':
		if len([x for x in visited.values() if x>=2])<2:
			ans.add(tuple(path))
		return
	elif root in visited and visited[root]==1 and root=='start':
		return
	elif (root in visited and visited[root]==2) or len([x for x in visited.values() if x==2])>1:
		return
	else:
		if(root==root.lower()):
			visited[root]+=1
		for x in graph[root]:
			dfs(x,visited,path+[x])
		if(root==root.lower()):
			visited[root]-=1
	return
dfs('start',visited,['start'])
print(len(ans))
