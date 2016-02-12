def primetrigger(x):
    trigger = 1
    i=2
    while i <=x**0.5:
        if ((x)%i ==0): trigger=0; break 
        i+=1
    return trigger
#while primenumber(new)!=1:
def primefactors(x):
    primefactor =[]
    new=x
    i=2
    while i <=new:
        #print new
        if primetrigger(new)==1:
            primefactor.append(new)
            new=new/new
        else:    
            if primetrigger(i) ==1 :
                if new%i==0 : 
                    primefactor.append(i)
                    new = new/i
                    i=1
        i+=1
    mydict=dict()
    mylist = primefactor
    try:
        for j in mylist:
            if j not in mydict:
                mydict[j]=1
            else:
                mydict[j]+=1
    except: pass
    return mydict

def divisorGen(x):
    primedict = primefactors(x)
    nfactors = len(primefactors(x).keys())
    f = [0]*nfactors
    count=0
    while True:
        count+=1
        #print [primedict.keys()[x]**f[x] for x in xrange(nfactors)]
        yield reduce(lambda x,y:x*y,[primedict.keys()[x]**f[x] for x in xrange(nfactors)],1)
        i=0
        while True:
            f[i]+=1
            if f[i]<=primedict[primedict.keys()[i]]:
                break
            f[i]=0
            i+=1
            if i>=nfactors:
                return

def abundantsum(x):
    i=0
    j=0
    while True:
        yield x[i]+x[j]
        #j=0
        while True:
            j+=1
            if j<len(x):
                break
            j=i
            i+=1
            if i>=len(x)-1:
                return
x=28123
abundantlist =[]
for i in xrange(1,x+1):
    if primetrigger(i)==0:
#        print i
        summation=0
        for j in divisorGen(i):
            summation+=j
        summation = summation-i
        if summation>i:
            abundantlist.append(i)

mylist = [True]*x
for i in xrange(len(abundantlist)):
    for j in xrange(i,len(abundantlist)):
        if abundantlist[i]+abundantlist[j]>=x:
            break
        else:
            mylist[abundantlist[i]+abundantlist[j]]=False

#alternative way to generate the list
mylist = [True]*x
for i in abundantsum(abundantlist):
    if i>=x:
        next #use next instead of break or else mylist will be incomplete
    else:
        mylist[i]=False
        print i


summation=0
for i,j in enumerate(mylist):
    if mylist[i]==True:
        summation+=i
        print i