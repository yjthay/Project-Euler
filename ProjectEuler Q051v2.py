def primetrigger(x):
    trigger = 1
    i=2
    while i <=x**0.5:
        if ((x)%i ==0): trigger=0; break 
        i+=1
    return trigger
def splicer(x):
     return int("".join(str(n) for n in x) )
     
def primesieve(maxnumber):

    psieve = [True]*maxnumber
    psieve[0] = psieve[1]= False
    for (i,isprime) in enumerate(psieve):
        if isprime:
            yield i
            for j in xrange(i,maxnumber,i):
                psieve[j]=False
                

digits = {i for i in xrange(10)}
number=10   
for number in primesieve(10000000):
    #if primetrigger(number)==1:
    mastertuple = [int(j) for j in str(number)]
    #print mastertuple
    numlist = [int(k) for k in str(number)]
    mindig = min(numlist)
    mindigcount=numlist.count(mindig)
    mindigindex = numlist.index(mindig)
    mindiglist = []
    counter =0
    if mindigindex!=0: 
        for i, j in enumerate(numlist):
            if j == mindig:
                mindiglist.append(i)
        #print number, mindigcount,mindiglist
        for i in digits:
            for j in mindiglist:
                numlist[j]=i
            #print numlist
            if primetrigger(splicer(numlist))==1:
                print splicer(numlist)
                numlist = [n for n in mastertuple]
                counter+=1
    if counter==8:
        break
    #number+=1
#print number

