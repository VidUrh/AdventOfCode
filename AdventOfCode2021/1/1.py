file = open("input.txt",'r');
lines=[int(x) for x in file.readlines()];
three=[(lines[x-1]+lines[x]+lines[x+1]) for x in range(1,len(lines)-1)]
print(three)
print(sum(1 for i,x in list(enumerate(three))[1:] if x>three[i-1]))
