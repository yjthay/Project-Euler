# -*- coding: utf-8 -*-
#Let d(n) be defined as the sum of proper divisors of n 
#(numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a ≠ b, then 
#a and b are an amicable pair and each of a and b are called amicable numbers.

#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 
#20, 22, 44, 55 and 110; therefore d(220) = 284. 
#The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

#Evaluate the sum of all the amicable numbers under 10000.

import itertools

a=221

def primetrigger(x):
    trigger = 1
    i=2
    while i <=x**0.5:
        if ((x)%i ==0): trigger=0; break 
        i+=1
    return trigger
#while primenumber(new)!=1:
def primefactors(x):
    primefactor =[]
    new=x
    i=2
    while i <=new:
        #print new
        if primetrigger(new)==1:
            primefactor.append(new)
            new=new/new
        else:    
            if primetrigger(i) ==1 :
                if new%i==0 : 
                    primefactor.append(i)
                    new = new/i
                    i=1
        i+=1
    mydict=dict()
    mylist = primefactor
    try:
        for j in mylist:
            if j not in mydict:
                mydict[j]=1
            else:
                mydict[j]+=1
    except: pass
    return mydict

def divisorGen(x):
    primedict = primefactors(x)
    nfactors = len(primefactors(x).keys())
    f = [0]*nfactors
    count=0
    while True:
        count+=1
        #print [primedict.keys()[x]**f[x] for x in xrange(nfactors)]
        yield reduce(lambda x,y:x*y,[primedict.keys()[x]**f[x] for x in xrange(nfactors)],1)
        i=0
        while True:
            f[i]+=1
            if f[i]<=primedict[primedict.keys()[i]]:
                break
            f[i]=0
            i+=1
            if i>=nfactors:
                return
    #print count
    
x=10000
amicablepair = []
for i in xrange(1,x):
    if primetrigger(i)==0:
        summation1=0
        #print i
        for j in divisorGen(i):
            summation1 +=j
        summation1 = summation1-i
        #print summation1
        if summation1<x and primetrigger(summation1)==0:
            summation2=0
            for j in divisorGen(summation1):
                summation2 +=j
            summation2=summation2-summation1
            if summation2==i and summation1!=i:
                amicablepair.append([i,summation1])

summation=0
for i in xrange(len(amicablepair)):
    summation +=amicablepair[i][0]
print summation