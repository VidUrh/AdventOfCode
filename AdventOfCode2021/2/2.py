file = open("input.txt",'r');
lines=[x.strip('\n').split() for x in file.readlines()];

horizontal=0;
vertical=0;
aim=0;


for x in lines:
    if x[0] == 'forward':
        horizontal+=int(x[1])
        vertical+=aim*int(x[1])
    elif x[0] == 'down':
        aim+=int(x[1])
    elif x[0] == 'up':
        aim-=int(x[1])

print(vertical*horizontal)
