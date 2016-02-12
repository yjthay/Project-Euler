import itertools
summation=0
divisor=[2,3,5,7,11,13,17]
for j in itertools.permutations(range(9,-1,-1),10):
    
    
    startingdig=1
    divisorused=0
    breaktrigger=0
    #i forgot about <=.. so missed out checking divisor=17
    while startingdig<=len(j)-3:
        mylist=[]
        for k in xrange(startingdig,startingdig+3):
            mylist.append(str(j[k]))
        dividend="".join(mylist)
        dividend=int(dividend)
        #print dividend,j, divisor[divisorused]
        if dividend%divisor[divisorused]!=0:
            breaktrigger=1
            break
        #print dividend,j, divisor[divisorused]
        divisorused+=1
        startingdig+=1
    if breaktrigger==0:
        number=[str(l) for l in j]
        mergenum=int("".join(number))
        summation+=mergenum
        print j, summation
            