from collections import Counter
from itertools import permutations as perm
from itertools import combinations as comb

"""f=open("input.txt",'r')
lines=[x.strip('\n') for x in f.readlines()]
line=lines[0].split()[2:]
x=line[0]
y=line[1]"""


x1=79
x2=137
y1=-176
y2=-117

x=0
step=0
while x<x2:
	step+=1
	x+=step
	if x>x1:
		break

range_x=max(x1,x2)
range_y=max(abs(y1),abs(y2))

maxi=0
unique=0
for y in range(-range_y,range_y+1):
	for x in range(-range_x,range_x+1):
		pos_x=0
		pos_y=0
		vel_x=x
		vel_y=y
		height=0
		while pos_x<=x2 and pos_y >=y1:
			pos_x+=vel_x
			pos_y+=vel_y
			vel_y-=1
			vel_x-=(vel_x > 0) - (vel_x < 0)
			height=max(pos_y,height)
			if x1<=pos_x<=x2 and y1<=pos_y<=y2:
				print(x,y)
				maxi=max(height,maxi)
				unique+=1
				break

print(maxi)
print(unique)






