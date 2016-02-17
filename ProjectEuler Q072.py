# -*- coding: utf-8 -*-
def primetrigger(x):
    trigger = 1
    i=2
    while i <=x**0.5:
        if ((x)%i ==0): trigger=0; break 
        i+=1
    return trigger
#while primenumber(new)!=1:
def uniqprime(x):
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
    return primefactor
    
#n	Relatively Prime	φ(n)	n/φ(n)
#2	1	                1	2
#3	1,2	                2	1.5
#4	1,3	                2	2
#5	1,2,3,4	                4	1.25
#6	1,5	                2	3
#7	1,2,3,4,5,6	        6	1.1666...
#8	1,3,5,7	                4	2
#9	1,2,4,5,7,8	        6	1.5
#10	1,3,7,9	                4	2.5

#using φ(n) = (p-1)(q-1) where n=p*q

def primecompiler(mylist):
    output=dict()
    for i in mylist:
        if i in output:
            output[i]+=1
        else:
            output[i]=1
    return output

def totient(x):
    count=1
    plist= primecompiler(uniqprime(x))
    for key in plist.keys():
        count*=(key-1)*(key**(plist[key]-1))
    return count
 
answer=0
for i in xrange(2,1000001):
    tot=totient(i)
    answer+=tot
print answer
