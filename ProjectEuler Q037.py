def primesieve(maxnumber):
    psieve = [True]*maxnumber
    psieve[0] = psieve[1]= False
    for (i,isprime) in enumerate(psieve):
        if isprime:
            yield i
            for j in xrange(i,maxnumber,i):
                psieve[j]=False
                
def primetrigger(x):
    trigger = 1
    i=2
    while i <=x**0.5:
        if ((x)%i ==0): trigger=0; break 
        i+=1
    if x==1:
        trigger=0
    return trigger

count=0
for i in primesieve(1000000):
    ilist=[j for j in str(i)]
    j=1
    if i >10:
        breaktrigger=0    
        while j<len(ilist):
            truncatedi="".join(ilist[j:])
            truncatedi=int(truncatedi)
            if primetrigger(truncatedi)==0:
                breaktrigger=1
                break
            else:
                truncatedi="".join(ilist[:-j])
                truncatedi=int(truncatedi)
                if primetrigger(truncatedi)==0:
                    breaktrigger=1
                    break
            j+=1
        if breaktrigger==0:
            count+=i
            print i,count