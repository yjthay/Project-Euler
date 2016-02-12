mylist=[]
for i in xrange(1,1000001):
    for digit in str(i):
        mylist.append(int(digit))
    

print mylist[1-1]
print mylist[10-1]
print mylist[100-1]
print mylist[1000-1]
print mylist[10000-1]
print mylist[100000-1]
print mylist[1000000-1]
print mylist[1-1]*mylist[10-1]*mylist[100-1]*mylist[1000-1]*mylist[10000-1]*mylist[100000-1]*mylist[1000000-1]

