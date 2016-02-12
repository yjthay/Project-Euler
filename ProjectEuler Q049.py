def primetrigger(x):
    trigger = 1
    i=2
    while i <=x**0.5:
        if ((x)%i ==0): trigger=0; break 
        i+=1
    return trigger

for i in xrange(1000,10000):
    for j in xrange(i,(10000-i)/2):
        mylist=[]
        i2= i+j
        i3=i+j*2
        perms =1
        if primetrigger(i)==1:
            if primetrigger(i2)==1:
                if primetrigger(i3)==1:
                    for digit in str(i):
                        mylist.append(digit)
                    for digit in str(i2):
                        if digit not in mylist:
                            perms=0
                            break
                    if perms !=0:
                        for digit in str(i3):
                            if digit not in mylist:
                                perms=0
                                break
                    if perms==1:
                        print i,j
                    
                        