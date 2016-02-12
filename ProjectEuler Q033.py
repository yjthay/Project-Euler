from decimal import *
mylist=[]
for i in xrange(10,100):
	for j in xrange(i, 101):
		fraction1=Decimal(i)/Decimal(j)
		#print fraction1
		listi=[digit for digit in str(i)]
		newi=listi[0]
		listj=[digit for digit in str(j)]
		newj=listj[1]
		#print i,newi,j,newj
		if listi[1]==listj[0] and int(newj)!=0 and i!=j:
			fraction2=Decimal(newi)/Decimal(newj)
			if fraction1==fraction2:
				mylist.append([i,j])
print mylist
product=1
for i,j in mylist:
	product*=Decimal(i)/Decimal(j)
