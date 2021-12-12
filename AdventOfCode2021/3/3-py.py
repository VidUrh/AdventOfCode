file = open("input.txt",'r');
lines = file.readlines();
gama = '000010111110';
e='111101000001';

gama='10110'
e='01001'
co2 = [x for x in lines]
o2 = [x for x in lines]
i=0
while len(co2)>1:
	enice=sum(1 for x in co2 if x[i]=='1')
	if(enice>=float(len(co2))/2):
		nextbit = '0'
	else:
		nextbit='1'
	
	co2= [x for x in co2 if x[i]==nextbit]
	i+=1
i=0
while len(o2)>1:
	enice=sum(1 for x in o2 if x[i]=='1')
	if(enice>=float(len(o2))/2):
		nextbit = '1'
	else:
		nextbit='0'
	o2= [x for x in o2 if x[i]==nextbit]
	i+=1
	
print(co2)
print(int(o2[0],2)*int(co2[0],2))
