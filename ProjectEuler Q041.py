def primetrigger(x):
    trigger = 1
    i=2
    while i <=x**0.5:
        if ((x)%i ==0): trigger=0; break 
        i+=1
    return trigger
    
import itertools

for i in xrange(9,0,-1):
    for j in itertools.permutations(range(i,0,-1),i):
        y = [str(k) for k in j]
        #print y
        y=int("".join(y))
        #print y
        if primetrigger(y)==1:
            print y
            break