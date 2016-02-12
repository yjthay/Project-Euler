def primetrigger(x):
    trigger = 1
    i=2
    while i <=x**0.5:
        if ((x)%i ==0): trigger=0; break 
        i+=1
    return trigger

def splicer(x):
     return int("".join(str(n) for n in x) )
crit=8
import itertools
#digits = {i for i in xrange(10)}
number= 1
while True:
    if primetrigger(number)==1:
        mastertuple = [int(j) for j in str(number)]
        #print mastertuple
        numlist = [int(k) for k in str(number)]
        mindig = min(numlist)
        mindiglist = []
        for i, j in enumerate(numlist):
            if j == mindig:
                mindiglist.append(i)
        digits = [i for i in xrange(mindig,10)]
        #if mindiglist[0]!=0 and len(mindiglist)!=1:
        for c in xrange(1,len(mindiglist)+1):
            for combi in itertools.combinations(mindiglist,c):
                counter=0
                for i in digits:
                    for mindigindex in combi:
                        numlist[mindigindex]=i
                    #print splicer(numlist)
                    if primetrigger(splicer(numlist))==1:
                        counter+=1
                    #print counter, splicer(numlist)
                    numlist = [n for n in mastertuple]
                    if counter==crit:
                        #print combi
                        break
                if counter==crit:
                    break
            if counter==crit:
                break            
        if counter==crit:
            break
    #if number==121313:
   #     break
    number+=1
print number