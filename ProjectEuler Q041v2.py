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

for i in primesieve(987654321):
    primelist.append(i)
    
for i in xrange(987654321,0,-1):
    if primetrigger(i)==1:
        mylist=[j for j in str(i)]
        mylist.sort()
        breaktrigger=0
        print i
        #print mylist[0]
        if mylist[0]=="0":
            next
        else:
            for j in xrange(len(mylist)):
                if j+1 <len(mylist):
                    if mylist[j]==mylist[j+1]:
                        breaktrigger=1
                        break
            if breaktrigger==0:
                print i
                break