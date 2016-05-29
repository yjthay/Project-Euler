# -*- coding: utf-8 -*-

def tot_iter(x,upper,lower):
    import fractions
    count=0
    for i in xrange(lower,upper+1):
        if fractions.gcd(i,x)==1:
            yield i

max=12001
import fractions
from fractions import Fraction
answer=[]

for d in xrange(1,max):
  upper=int(d*1/2)+1
  lower=int(d*1/3)-1
  for n in tot_iter(d,upper,lower):
    new=Fraction(n,d)
    #print n,d
    if Fraction(1,3)<new<Fraction(1,2):
      answer.append(new)
      print n,d
print len(answer)
    