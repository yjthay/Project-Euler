digits= [1,2,3,4,5,6,7,8,9]
holytrinity=[]
for i in xrange(101,10000):
    for j in xrange(1,101):
        multiplication=i*j
        #print multiplication, i,j
        mylist=[]
        for digit in str(multiplication):
            mylist.append(digit)
        for digit in str(i):
            mylist.append(digit)
        for digit in str(j):
            mylist.append(digit)
        mylist.sort()
        if len(mylist)!=9 or mylist[0]=="0":
            next
        else:
            for k in xrange(len(mylist)-1):
                if mylist[k]==mylist[k+1]:
                    break
            if mylist[k]!=mylist[k+1]:
                holytrinity.append([i,j,multiplication])
                print holytrinity
                
summationlist=[]
for i,j,k in holytrinity:
    if k not in summationlist:
        summationlist.append(k)

print sum(summationlist)