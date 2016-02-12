#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def primenumber(x):
    trigger = 1
    i=2
    while i <x:
        if ((x)%i ==0): trigger=0; break 
        i+=1
    return trigger

primefactor =0
x =input("What is the number in question")
new=x
#while primenumber(new)!=1:
for j in xrange(0,10):
    i=2
    new1=new
    while i <new:
        if primenumber(new)==1: break
        else:    
            if primenumber(i) ==1 :
                if new%i==0 : 
                    primefactor =i
                    new = new/primefactor
                    break
        i+=1
    print new; print primefactor
    



#after revising this might be a better and neater way which i can use for other problems

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
    while i <new:
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
    print primefactor