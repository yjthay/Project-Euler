
def infperiodgen(S):
    if (S**0.5).is_integer():
        yield [int(S**0.5)]
    else:
        a0=int(S**0.5)
        a=int(S**0.5)
        m=0
        d=1
        answerlist=[]
        output=[]
        count=0
        #print m,d,a
        while True:
            answerlist.append([m,d,a])
            output.append(a)
            yield output
            count+=1
            #print m,d,a
            m=d*a-m
            d=(S-m**2)/d
            a=int((a0+m)/d)
        count-=1
    #return output

def ContFracAgg(mylist):
    import fractions
    from fractions import Fraction
    ans=0
    i=len(mylist)-1
    while i>=1:
        ans=Fraction(1,mylist[i]+ans)
        i-=1
    ans+=mylist[0]
    return ans


answerlist=[]
for D in xrange(2,1001):
    if (D**0.5).is_integer():
        next
    else:
        for mylist in infperiodgen(D):
            frac=ContFracAgg(mylist)
            x=frac.numerator
            y=frac.denominator
            #print x,y,D
            if x**2-D*(y**2)==1:
                break
        answerlist.append([x,D])
    #print D
answerlist.sort()
print answerlist[-1]