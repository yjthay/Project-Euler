#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.
def noobprimesieve(maxnumber):
    #maxnumber = 100
    #return a list of prime numbers under the variable input into the function
    limit= int(ceil(maxnumber**0.5))
    psieve1 = [i for i in range(2,maxnumber+1)]
    psieve2=[]
    for j in range(0,limit):
        removalfactor = min(psieve1)
        psieve2.append(min(psieve1))
        sievelist = [removalfactor*i for i in range(1,maxnumber/2+1)]
        for i in sievelist:
            try:
                psieve1.remove(i)
            except:
                pass
    output = psieve2+psieve1
    return output
    #removalfactor
    #for i in 
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
def primesieve(maxnumber):

    psieve = [True]*maxnumber
    psieve[0] = psieve[1]= False
    for (i,isprime) in enumerate(psieve):
        if isprime:
            yield i
            for j in xrange(i,maxnumber,i):
                psieve[j]=False

outputlist = []
outputlist = [i for i in primesieve(2000000)]
sum = 0
for i in outputlist:
    sum+=i
print sum
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
i=2
sum = 0
primenumberlist=[]
while i < 2000000:
    for j in xrange(0,len(primenumberlist)):
        if i%primenumberlist[j]==0: break
    if primenumber(i)==1:
        primenumberlist.append(i)
        sum +=i
        #print i
    i+=1
print sum,primenumberlist

sum1=0
for i in primenumberlist:
    sum1=i+sum1
print sum1

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

def primenumber(x):
    trigger = 1
    i=2
    while i <x**2:
        if ((x)%i ==0): trigger=0; break 
        i+=1
    return trigger

#i=2
#sum = 0
#while i < 2000000:
#    if primenumber(i)==1:
#        sum +=i
#        #print i
#    i+=1
#print sum
i=2
sum = 0
primenumberlist=[]
while i < 1000:
    for j in xrange(0,len(primenumberlist)):
        if i%primenumberlist[j]==0: print i; break
    if primenumber(i)==1:
        primenumberlist.append(i)
        print primenumberlist
        sum +=i
        print i
    i+=1
print sum


142913828926


