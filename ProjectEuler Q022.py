fname = "C:\Users\YJ\OneDrive\Documents\Project Euler\Grids\Project Euler Q22 Names.txt"

fhand = open(fname)

mylist = "abcdefghijklmnopqrstuvwxyz"

i=1
for alphabet in mylist:
    mydict[alphabet] = i
    i+=1
print mydict

namepost=1
totalsum = 0
for line in fhand:
    line.rstrip()
    names = line.split(",")
    names.sort()
    for name in names:
        namesum=0
        for alphabet in name.lower():
            if alphabet!='"':
                namesum += mydict[alphabet]
        totalsum += namesum*namepost
        namepost+=1
        