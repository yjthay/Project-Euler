import math
x=math.factorial(9)
mylist=[]
for i in xrange(3,x):
	summation=0
	for digit in str(i):
		summation+=math.factorial(int(digit))
	if summation==i:
		mylist.append(i)
		
print sum(mylist)
