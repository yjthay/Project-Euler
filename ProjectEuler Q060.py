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

import itertools
combi = []
breaktrigger=0

for x1 in xrange(len(primeset)):
    combi=[primeset[x1]]
    for x2 in xrange(x1+1, len(primeset)):
        combi=[primeset[x1],primeset[x2]]
        if twowayconc(combi)==1:
            #print combi
            for x3 in xrange(x2+1, len(primeset)):
                combi=[primeset[x1],primeset[x2],primeset[x3]]
                if twowayconc(combi)==1:
                    for x4 in xrange(x3+1, len(primeset)):
                        combi=[primeset[x1],primeset[x2],primeset[x3],primeset[x4]]
                        if twowayconc(combi)==1:
                            #print combi
                            for x5 in xrange(x4+1, len(primeset)):
                                combi=[primeset[x1],primeset[x2],primeset[x3],primeset[x4],primeset[x5]]
                                #print combi
                                if twowayconc(combi)==1:
                                    print combi
                                    breaktrigger=1
                                    break
                        if breaktrigger==1:
                            break
                if breaktrigger==1:
                    break
        if breaktrigger==1:
            break
    if breaktrigger==1:
        break

                                
