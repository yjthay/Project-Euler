
#num=1+1/x1
#x1=2+1/x2
#x2=2+1/x3
import fractions
from decimal import *
myothercontext = Context(prec=50, rounding=ROUND_HALF_DOWN)
setcontext(myothercontext)

answer=0
limit=1000
replist=[0]*(limit-1)
replist.append(2)
for rep in xrange(limit-1,0,-1):
    x=Fraction(2+1/replist[rep])
    replist[rep-1]=x
    number=1+1/x
    #print number
    numeratorcount=0
    denominatorcount=0
    number= fractions.Fraction(number)
    for i in str(number.numerator):
        numeratorcount+=1
    for i in str(number.denominator):
        denominatorcount+=1
    if numeratorcount>denominatorcount:
        answer+=1
        #print number , numeratorcount,denominatorcount

print answer