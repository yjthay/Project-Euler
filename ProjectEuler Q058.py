def primetrigger(x):
    trigger = 1
    i=2
    while i <=x**0.5:
        if ((x)%i ==0): trigger=0; break 
        i+=1
    return trigger

prime = 0
nonprime= 1
ratio=1
length = 1
i=1
diagnum=1
while ratio>0.1:
    for corners in xrange(1,5):
        diagnum = i+length+1
        i=diagnum
        #print i
        if primetrigger(i)==1:
            prime+=1.0
            #print i
        else:
            nonprime+=1.0
    ratio = (prime/(prime+nonprime))
    length+=2
print ratio, length    