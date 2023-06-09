f = open("day2.txt")

lines = f.readlines()

def evaluate(opp,you):

    yourScore = "XYZ".index(you)+1

    you = "XYZ".index(you)
    opp = "ABC".index(opp)

    if you == opp:
        return yourScore+3
    elif (you == 1 and opp == 0) or (you == 2 and opp == 1) or (you == 0 and opp == 2):
        return yourScore + 6
    else:
        return yourScore
val = 0
for line in lines:
    opp,you = line.split()
    if opp == 'A':
        if you == "Y":
            you = "X"
        elif you == "X":
            you = "Z"
        elif you == "Z":
            you = "Y"
    if opp == "B":
        if you =="Y":
            you = "Y"
        elif you == "X":
            you = "X"
        elif you == "Z":
            you = "Z"
    if opp == "C":
        if you =="Y":
            you = "Z"
        elif you == "X":
            you = "Y"
        elif you == "Z":
            you = "X"
    
    print(opp,chr(ord(you)-23))
    val += evaluate(opp,you)

print(val)