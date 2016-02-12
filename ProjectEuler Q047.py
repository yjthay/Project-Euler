def primetrigger(x):
    trigger = 1
    i=2
    while i <=x**0.5:
        if ((x)%i ==0): trigger=0; break 
        i+=1
    return trigger
#while primenumber(new)!=1:
def uniqueP(x):
    primefactor =[]
    new=x
    i=2
    while i <new:
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
    mylist=[]
    primefactor.sort()
    for i in primefactor:
        if i not in mylist:
            mylist.append(i)
    mylist1=[]
    for i in mylist:
        count=0
        for j in primefactor:
            if i==j:
                count+=1
        mylist1.append(i**count)
        
    return mylist1

mylist = []
for i in xrange(100,10000000):
    if len(uniqueP(i))==4:
        if len(uniqueP(i+1))==4:
            if len(uniqueP(i+2))==4:
                if len(uniqueP(i+3))==4:
                    mylist+=uniqueP(i)
                    mylist+=uniqueP(i+1)
                    mylist+=uniqueP(i+2)
                    mylist+=uniqueP(i+3)
                    #mylist.append(primefactorization(i))
                    #mylist.append(primefactorization(i))
                    mylist.sort()
                    #print mylist
                    duplicate=0
                    for j in xrange(len(mylist)):
                        if j+1>=len(mylist):
                            break
                        else:
                            if mylist[j]==mylist[j+1]:
                                duplicate =1
                    if duplicate==0:
                        print i
                        break
                    mylist=[]