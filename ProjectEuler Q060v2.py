def primetrigger(x):
    trigger = 1
    i=2
    while i <=x**0.5:
        if ((x)%i ==0): trigger=0; break 
        i+=1
    return trigger

def twowayconc(mylist):
    import itertools
    for pair in itertools.combinations(mylist,2):
        num=int(str(pair[0])+str(pair[1]))
        reversenum=int(str(pair[1])+str(pair[0]))
        if primetrigger(num)!=1 or primetrigger(reversenum)!=1:
            return 0
    return 1
  
def primesieve(maxnumber):
    psieve = [True]*maxnumber
    psieve[0] = psieve[1]= False
    for (i,isprime) in enumerate(psieve):
        if isprime:
            yield i
            for j in xrange(i,maxnumber,i):
                psieve[j]=False

primeset = [i for i in primesieve(10000)]

combi = []
answerlist=[]
for x1 in xrange(len(primeset)):
    combi=[]
    combi.append(primeset[x1])
    for x2 in xrange(x1+1, len(primeset)):
        combi.append(primeset[x2])
        #print combi,x1,x2
        if twowayconc(combi)==1:
            for x3 in xrange(x2+1, len(primeset)):
                combi.append(primeset[x3])
                if twowayconc(combi)==1:
                    for x4 in xrange(x3+1, len(primeset)):
                        combi.append(primeset[x4])
                        if twowayconc(combi)==1:
                            for x5 in xrange(x4, len(primeset)):
                                combi.append(primeset[x5])
                                #print combi
                                if twowayconc(combi)==1:            
                                    answerlist.append(combi)
                                    #print combi
                                else:
                                    combi.remove(primeset[x5])
                                    next                                   
                        else:
                            combi.remove(primeset[x4])
                            next
                else:
                    combi.remove(primeset[x3])
                    next
        else:
            combi.remove(primeset[x2])
            next
            
            
