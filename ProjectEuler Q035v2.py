def primesieve(maxnumber):

    psieve = [True]*maxnumber
    psieve[0] = psieve[1]= False
    for (i,isprime) in enumerate(psieve):
        if isprime:
            yield i
            for j in xrange(i,maxnumber,i):
                psieve[j]=False

primelist=[]                
for i in primesieve(1000000):
    primelist.append(i)

def circgen(x):
    import string
    digits=[digit for digit in str(x)]
    ndigits=len(digits)
    f=[]
    j=0
    for i in xrange(ndigits):
        f.append(i)
        #print f
    while j<ndigits:
        yield int("".join([digits[f[i]] for i in xrange(ndigits)]))
        for i in xrange(ndigits):
            if f[i]==ndigits-1:
                f[i]=0
            else:
                f[i]+=1
        #print f
        j+=1
def primetrigger(x):
    trigger = 1
    i=2
    while i <=x**0.5:
        if ((x)%i ==0): trigger=0; break 
        i+=1
    return trigger
    
count=0

for i in primelist:
    breaktrigger=0
    for j in circgen(i):
        if primetrigger(j)==0:
            breaktrigger=1
    if breaktrigger==0:
        count+=1
        print count,i
            
        
        
        