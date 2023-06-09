f = open("day5.txt",'r')
lines = [x.strip('\n') for x in f.readlines()]
cargo = []

for i,x in enumerate(lines):
    if len(x) == 0:
        lines = lines[i+1:]
        break
    else:
        cargo.append(x)

cargo = cargo[:-1]

stacks = [[] for x in range(9)]
for line in cargo:
    for i,char in enumerate(line):
        if char.isalpha():
            stacks[i//4].append(char)
        
stacks = [i[::-1] for i in stacks]

for x in lines:
    s = x.split()
    num = int(s[1])
    prvi = int(s[3])
    drugi = int(s[5])
    [stacks[drugi-1].append(x) for x in (stacks[prvi-1][-num:])]
    stacks[prvi-1] = stacks[prvi-1][:-num]
print(*stacks)
print(''.join(x[-1]for x in stacks))