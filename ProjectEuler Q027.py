# -*- coding: utf-8 -*-
#n² + an + b, where |a| < 1000 and |b| < 1000

#where |n| is the modulus/absolute value of n
#e.g. |11| = 11 and |−4| = 4

def primesieve(maxnumber):
    psieve = [True]*maxnumber
    psieve[0] = psieve[1]= False
    for (i,isprime) in enumerate(psieve):
        if isprime:
            yield i
            for j in xrange(i,maxnumber,i):
                psieve[j]=False

def primetrigger(x):
    trigger = 1
    i=2
    while i <x:
        if ((x)%i ==0): trigger=0; break 
        i+=1
    if x<0: trigger=0
    return trigger

def quad(n,a,b):
    return n**2 + a*n + b
#xrange(-limit+1, limit)
breaktrigger=0
limit =1000
mylist =[]
for a in xrange(-limit+1, limit):
    for b in xrange(-limit+1, limit):
        n=0
        while True:
            if primetrigger(quad(n,a,b))==1:
                n+=1
                #print n,a,b,quad(n,a,b),primetrigger(quad(n,a,b))
                if primetrigger(quad(n+1,a,b))==0:
                    mylist.append([n,[a,b]])
                    print n,a,b,quad(n,a,b),primetrigger(quad(n,a,b))
                    break
            else:
                break

        #print a,b
                                
#for i in primesieve(100):
 #   print i