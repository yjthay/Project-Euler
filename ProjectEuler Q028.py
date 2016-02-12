#1001 by 1001

spiralsize = 1001
sumdiag=0
counter=[]
for i in xrange(1,spiralsize):
    if i%2!=0:
        counter.append(i)
counterinter=0
counterouter=0
holderi=1
while i<spiralsize**2:
    for i in xrange(holderi, spiralsize**2+1,counter[counterouter]+1):
        if counterinter<4:
            #print i
            sumdiag+=i
            counterinter+=1
        else:
            
            counterinter=0
            counterouter+=1
            holderi = i
            break

print sumdiag+spiralsize**2
    
    