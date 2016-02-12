def checkodd(x):
    if x%2!=0:
        print 1
    else:
        print 0
        
def primetrigger(x):
    trigger = 1
    i=2
    while i <=x**0.5:
        if ((x)%i ==0): trigger=0; break 
        i+=1
    return trigger
    
def primesieve(maxnumber):

    psieve = [True]*maxnumber
    psieve[0] = psieve[1]= False
    for (i,isprime) in enumerate(psieve):
        if isprime:
            yield i
            for j in xrange(i,maxnumber,i):
                psieve[j]=False
                
def goldbach(x):
    trigger = 0
    for i in primesieve(x):
        remainder = x-i
        remainder = remainder/2
        remainder = remainder**0.5
        if remainder.is_integer():
            trigger=1
    return trigger

for i in xrange(1,10000000,2):
    if primetrigger(i)==0:
        if goldbach(i)==0:
            print i
            break
        #    break

