
   
file = open("input.txt",'r');

graph={};
for line in file.readlines():
    parent,child = line.strip('.\n').split('contain');
    parent = parent.split()
    parent = parent[0]+parent[1]
    children = child.split(', ')
    children = [(x[1]+x[2],x[0]) for x in  [y.split() for y in children]]
    
    if(children!=[('otherbags', 'no')]):
        graph[parent]=children
    

def dfs(root):
    root,num=root
    num=int(num);
    if root not in graph:
        return num
    else:
        suma=0
        for x in graph[root]:
            temp=dfs(x);
            suma+=int(temp)
        return num*(suma+1)

    
print(dfs(('shinygold',1))-1)
