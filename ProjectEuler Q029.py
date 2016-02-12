limit=100
limit+=1

mylist = []
for a in xrange(2,limit):
    for b in xrange(2,limit):
        if a**b not in mylist:
            mylist.append(a**b)
            