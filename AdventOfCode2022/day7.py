f = open("day7.txt",'r')
commands = [x.strip() for x in f.readlines()]

currentDir = ['/']

file = open("temp.txt",'w')

def visualize(path, indent=0):
    for x in tree[path]:
        if x[0] == "dir":
            file.write("\t"*indent + f"{x[1]}: \n")
            visualize(path+'/'+x[1], indent+1)
        else:
            file.write("\t"*indent + repr(x[1]) +'\n')






sizes = float("inf")
minimum = abs(70000000 - 44795677 -30000000)
def dfs(tree,key):
    global sizes
    global minimum
    vsota = 0
    for x in tree[key]:
        if x[0] == "dir":
            vsota+=dfs(tree,key+'/'+x[1])
        else:
            vsota+=int(x[0])
    if vsota > minimum:
        sizes = min(sizes,vsota)
    return vsota


tree = {'/':[]}
i = 0
while i < len(commands):
    line = commands[i]
    if line.startswith('$'):
        command = line.split()
        if command[1] == 'cd':
            if command[2] == '/':
                currentDir = ['/']
            elif command[2] == '..':
                currentDir = currentDir[:-1]
            else:
                currentDir.append(command[2])    
                if '/'.join(currentDir) not in tree:
                    tree['/'.join(currentDir)] = []
        else:
            pass
    else:
        tree['/'.join(currentDir)].append(commands[i].split())
    i+=1

visualize('/')
file.close()
print(dfs(tree,'/'))
print(sizes)