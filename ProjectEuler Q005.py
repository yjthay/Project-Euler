#Project Euler Q5
#2520 is the smallest number that can be divided by 
#each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly 
#divisible by all of the numbers from 1 to 20?

trigger = 0
j =21
number =j
#and number<3000
while trigger == 0 :
    listfailtrigger=0
    mylist=[]
    for i in xrange(1,j):
        mylist.append(number%i)
    for i in xrange(0,j-1):
        if mylist[i] != 0:
            listfailtrigger =1
    #print mylist
    if listfailtrigger ==1:
        trigger = 0
    else:
        trigger = 1
        print "The is the magic number is: " + str(number) + "!!!"
    number +=1
    #print number

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx

def primetrigger(x):
    trigger = 1
    i=2
    while i <x:
        if ((x)%i ==0): trigger=0; break 
        i+=1
    return trigger
#while primenumber(new)!=1:
def primefactorization(x):
    primefactor =[]
    new=x
    i=2
    while i <= new:
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

x=21  
mylist=[[1],[2]]
for i in range(3,x):
    mylist.append(primefactorization(i))
mylist

#by eyeballing 1*2*3*2*5*7*2*3*11*13*2*17*19