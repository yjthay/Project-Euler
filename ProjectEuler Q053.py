import itertools
count=0

def combi(n,r):
	import math
	return math.factorial(n)/math.factorial(n-r)/math.factorial(r)

for n in xrange(1,101):
	for r in xrange(1,n+1):
		counter=combi(n,r )
		if counter>1000000:
			count+=1
print count
