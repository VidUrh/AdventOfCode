f = open("day1.txt")

lines = ' '.join(f.readlines())
t = [x.strip() for x in lines.split(" ")]
t = '+'.join(t)
t = t.split('++')
sume = [eval(x) for x in t]
sume.sort(reverse=True)
print(sum([sume[0],sume[1],sume[2]]))