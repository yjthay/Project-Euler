#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
#we can see that the 6th prime is 13.
#What is the 10 001st prime number?

def primetrigger(x):
    trigger = 1
    i=2
    while i <x:
        if ((x)%i ==0): trigger=0; break 
        i+=1
    return trigger

i=2
primecounter=0
while primecounter <10001:
    if primetrigger(i)==1:
        primecounter+=1
        print i
    i+=1
    