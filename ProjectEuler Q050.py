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
    return trigger
    
maxnumber=1000000
primelist=[]
#10,000 is used as a best guess
for i in primesieve(10000):
    primelist.append(i)


summation=0
back=0
maxj=0
for i in xrange(len(primelist)):
    #print i
    for j in xrange(i+maxj,len(primelist)):
        summation=0
        back=0
        back=i+j
        for k in primelist[i:back]:
            summation+=k
        #print i, back, summation
        if summation<maxnumber:
            if primetrigger(summation)==1:
                if j>maxj:
                    maxj=j
                    print "This is maxj", i, j, summation
        else:
            break