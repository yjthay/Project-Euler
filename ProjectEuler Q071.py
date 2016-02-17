# coding: utf-8


                
max=1000001
import fractions
from fractions import Fraction
answer=0
for d in xrange(1,max):
  nume=int(d*3/7)+1
  for n in xrange(nume,1,-1):
    new=Fraction(n,d)
    if new<answer:
      break
    elif new<Fraction(3,7):
      answer=new
      #print answer
      break
print answer
    