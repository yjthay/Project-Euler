i=1

def listdig(x):
	mylist=[]
	for digits in str(x):
		mylist.append(digits)
	return mylist

while True  :
	masterlist=[]
	duplicate=1
	ilist=[(i*j) for j in xrange(1,7)]
	#print ilist
	for j in ilist:
		masterlist.append(listdig(j))
	firstcopy=[]
	for jlist in masterlist:
		number=0
		jlist.sort()
		for k in jlist:
			if len(firstcopy)!=len(jlist):
				firstcopy.append(k)
				#print firstcopy
			else:
				if firstcopy[number]!=k:
					duplicate=0
					break
			number+=1
	if duplicate==1:
		break
	#print masterlist
	i+=1
print i
