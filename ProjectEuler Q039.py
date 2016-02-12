mylist=[]
for a in xrange(1,1001):
    for b in xrange(a,1001):
        for c in xrange(b,1001):
            perimeter = a+b+c
            if a**2+b**2==c**2 and perimeter<=1000:
                mylist.append([perimeter,1])
            else:
                next

countlist=[]    
for i,j in mylist:
    if i not in countlist:
        countlist.append(i)
 
mycount=[]      
for i in countlist:
    sumcount=0
    for j, k in mylist:
        if j==i:
            sumcount+=1
    mycount.append([sumcount,i])
    
print max(mycount)