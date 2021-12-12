f = open("input.txt",'r')
lines = f.readlines();
vse=0
for x in lines:
	data,out = x.split('|')
	data=data
	out=out.split()
	
	c = {x:data.count(x) for x in data}
	data = data.split();
	
	
	sedem = [x for x in data if len(x)==3][0]
	ena = [x for x in data if len(x)==2][0]
	stiri = [x for x in data if len(x)==4][0]

	zgorej = [x for x in sedem if x not in ena][0]
	zgDesno = [x for x in c if c[x]==8 and x!=zgorej][0]
	spDesno = [x for x in c if c[x]==9][0]
	sredina = [x for x in c if c[x]==7 and x in stiri][0]
	levoZg = [x for x in c if c[x]==6][0]
	levoSp = [x for x in c if c[x]==4][0]
	spodej = [x for x in c if c[x]==7 and x not in stiri][0]
	
	ans=''
	for y in out:
		
		if len(y)==2:
			ans+='1'
		
		elif len(y)==3:
			ans+='7'
		
		elif len(y)==4:
			ans+='4'
		
		elif len(y)==7:
			ans+='8'
			
		elif sorted(y)==sorted([zgorej,spDesno,zgDesno,levoZg,levoSp,spodej]):
			ans+='0'
		
		elif sorted(y)==sorted([zgorej,zgDesno,levoSp,spodej,sredina]):
			ans+='2'
			
		elif sorted(y)==sorted([zgorej,spDesno,levoZg,spodej,sredina]):
			ans+='5'

		elif sorted(y)==sorted([zgorej,zgDesno,spDesno,spodej,sredina]):
			ans+='3'	
				
		elif sorted(y)==sorted([zgorej,spDesno,levoZg,spodej,sredina,levoSp]):
			ans+='6'

		elif sorted(y)==sorted([zgorej,zgDesno,levoZg,spodej,sredina,spDesno]):
			ans+='9'
	vse+=int(ans);

print(vse)
