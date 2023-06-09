f = open("day10.txt",'r')
instructions = [x.strip() for x in f.readlines()]

cycle = 1
i = 0
x = 1
v = 0

pixel = 0

intervals = range(20,230,40)
out=0
t = False
while pixel < 225 and i<len(instructions):
    inst = instructions[i].split()
    print(['#',' '][abs(pixel-x)>1],end='')

    if inst[0] == "noop":
        i+=1
        pass
    else:
        if t:
            x+=int(inst[1])
            t=False
            i+=1
        else:
            t=True
    
    cycle+=1
    pixel+=1
    if pixel>39:
        print()
        pixel = 0

    