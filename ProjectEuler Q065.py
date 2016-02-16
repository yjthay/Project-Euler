# referred to algo from https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion
periodlist=[]    
convergence=100
convergence=convergence-2

elist=[2,1]
count=1
for i in xrange(0,convergence):
    if i%3!=0:
        elist.append(1)
    else:
        elist.append(2*count)
        count+=1
        
def ContFracAgg(mylist):
    ans=0
    i=len(mylist)-1
    while i>=1:
        ans=Fraction(1,mylist[i]+ans)
        i-=1
    ans+=mylist[0]
    return ans

print str(ContFracAgg(elist))

summation=0
for digit in str(ContFracAgg(elist).numerator):
    summation+=int(digit)

print summation