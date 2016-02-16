# referred to algo from https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion
periodlist=[]    
for S in xrange(1,10001):
    if (S**0.5).is_integer():
        next
    else:
        a0=int(S**0.5)
        a=int(S**0.5)
        m=0
        d=1
        answerlist=[]
        count=0
        #print m,d,a
        while [m,d,a] not in answerlist:
            answerlist.append([m,d,a])
            count+=1
            #print m,d,a
            m=d*a-m
            d=(S-m**2)/d
            a=int((a0+m)/d)
        count-=1
        if count%2!=0:
            periodlist.append([count,S])
        #print count
print len(periodlist)
#[m,d,a] not in answerlist