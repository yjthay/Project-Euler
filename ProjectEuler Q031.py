factors= [[1,200],[2,100],[5,40],[10,20],[20,10],[50,4],[100,2],[200,1]]
#factors = [[100,2],[50,4],[20,10],[10,20],[5,40],[2,100],[1,200]]

#
nfactors = len(factors)
f=[0]*nfactors
count=0
mysum=0
while True:
    mysum=0
    mysum = sum([factors[x][0]*f[x] for x in xrange(nfactors)])
    #reduce(lambda x,y:x+y,[factors[x][0]*f[x] for x in xrange(nfactors)],1)
    #print mysum, [factors[x][0]*f[x] for x in xrange(nfactors)]
    if mysum == 200:
        count+=1
        print count,[factors[x][0]*f[x] for x in xrange(nfactors)],f
    i=0
    while True:
        f[i]+=1
        summation = sum([factors[x][0]*f[x] for x in xrange(nfactors)])
        if f[i]<=factors[i][1] and summation<=200:
            break
        f[i]=0
        i+=1
        #print i
        if i>=nfactors:
            break
    if i>=nfactors:
        break
        