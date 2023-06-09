class Monkey:
    def __init__(self,opis):
        self.name = opis[0][:-1]
        self.startingItems = [int(x.strip(',')) for x in opis[1].split()[2:]]
        self.operation =  ' '.join(opis[2].split()[3:])
        self.test = int(opis[3].split()[-1])
        self.throwTrue = opis[4].split()[-1]
        self.throwFalse = opis[5].split()[-1]
        self.numInspections = 0
        self.commonModulo = 0

    def inspectItem(self):
        old = self.startingItems[0]
        self.startingItems[0] = int(eval(self.operation.replace("old",str(old))))
        #print(self.commonModulo)
        self.startingItems[0] %= self.commonModulo
        self.numInspections+=1
    
    def throwItem(self,monkeys):
        worryLevel = self.startingItems.pop(0)
        if worryLevel % int(self.test)==0:
            monkeys[int(self.throwTrue)].recieveItem(worryLevel)
        else:
            monkeys[int(self.throwFalse)].recieveItem(worryLevel)

    def recieveItem(self,worryLevel):
        self.startingItems.append(worryLevel)


    def makeTurn(self,monkeys):
        for _ in range(len(self.startingItems)):
            self.inspectItem()
            self.throwItem(monkeys)
            
f = open("day11.txt",'r')
monkeys1 = [x.strip() for x in f.readlines()]+['']
buf = []
monkeys = []


for a in monkeys1:
    buf.append(a)
    if len(a)==0:
        monkey = Monkey(buf)
        buf = []
        monkeys.append(monkey)

i=1
for monkey in monkeys:
    i*=monkey.test
print(i)
for monkey in monkeys:
    monkey.commonModulo = i


for _ in range(10000):
    for monkey in monkeys:
        monkey.makeTurn(monkeys)

temp = sorted([monkey.numInspections for monkey in monkeys])
print(temp)
print(temp[-1]*temp[-2])